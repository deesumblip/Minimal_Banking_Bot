"""Tutorial-compatible banking sub-agent (extends MCPOpenAgent).

The default ReAct loop passes ``tools=`` on every LLM call. The Rasa tutorial host
(``provider: rasa``) does not accept that API shape. This class routes user text to
MCP tools with simple rules, then uses the same ``model_group`` for **text-only**
completions so Level 6 demos work with ``RASA_LICENSE`` only.
"""

from __future__ import annotations

import re
from typing import Dict, Optional, Tuple

from rasa.agents.constants import KEY_CONTENT, KEY_ROLE
from rasa.agents.core.types import AgentStatus
from rasa.agents.protocol.mcp.mcp_open_agent import MCPOpenAgent
from rasa.agents.schemas import AgentInput, AgentOutput
from rasa.agents.schemas.agent_tool_result import AgentToolResult
from rasa.core.channels import OutputChannel
from rasa.shared.constants import ROLE_SYSTEM, ROLE_USER
from rasa.shared.providers.llm.llm_response import LLMResponse


class BankingAssistantLiteAgent(MCPOpenAgent):
    """MCP-backed specialist: deterministic tool routing + optional NLG without tool APIs."""

    async def send_message(
        self,
        agent_input: AgentInput,
        output_channel: Optional[OutputChannel] = None,
    ) -> AgentOutput:
        if not self._mcp_tools:
            await self.connect_to_servers()
            await self.fetch_and_store_available_tools()

        user_text = (agent_input.user_message or "").strip()
        lower = user_text.lower()

        if not lower:
            return AgentOutput(
                id=agent_input.id,
                status=AgentStatus.INPUT_REQUIRED,
                response_message=(
                    "What would you like to do? I can check a balance (give an account "
                    "number), transfer money between accounts, or look up account info."
                ),
                structured_results=self._get_structured_results_for_agent_output(
                    agent_input, {}
                ),
            )

        if not self._looks_like_banking_request(lower):
            text = await self._text_only_reply(
                agent_input,
                system=(
                    "You are a concise banking specialist. Reply in 1–3 short sentences. "
                    "Mention that you can check balances, move money, or show account "
                    "details when the user provides account numbers or transfer details."
                ),
                user=user_text,
            )
            return AgentOutput(
                id=agent_input.id,
                status=AgentStatus.INPUT_REQUIRED,
                response_message=text,
                structured_results=self._get_structured_results_for_agent_output(
                    agent_input, {}
                ),
            )

        routed = await self._route_to_tools(user_text, lower)
        if routed is None:
            text = await self._text_only_reply(
                agent_input,
                system=(
                    "You are a banking specialist. The user wants banking help but "
                    "did not give enough structured detail. Ask clearly for account "
                    "numbers (4+ digits) and, for transfers, amount and from/to accounts."
                ),
                user=user_text,
            )
            return AgentOutput(
                id=agent_input.id,
                status=AgentStatus.INPUT_REQUIRED,
                response_message=text,
                structured_results=self._get_structured_results_for_agent_output(
                    agent_input, {}
                ),
            )

        raw, tool_results = routed
        final = await self._text_only_reply(
            agent_input,
            system=(
                "You are a banking specialist. The factual answer below comes from "
                "banking tools—repeat it faithfully, in friendly natural language, "
                "1–4 sentences. Do not invent numbers."
            ),
            user=f"User request: {user_text}\n\nTool output:\n{raw}",
        )
        return AgentOutput(
            id=agent_input.id,
            status=AgentStatus.COMPLETED,
            response_message=final,
            structured_results=self._get_structured_results_for_agent_output(
                agent_input, tool_results
            ),
        )

    def _looks_like_banking_request(self, lower: str) -> bool:
        if any(
            k in lower
            for k in (
                "balance",
                "transfer",
                "account",
                "how much",
                "bank",
                "deposit",
            )
        ):
            return True
        return bool(re.search(r"\b(send|move|pay|wire)\b", lower))

    async def _route_to_tools(
        self, user_text: str, lower: str
    ) -> Optional[Tuple[str, Dict[str, AgentToolResult]]]:
        nums = re.findall(r"\b\d{4,}\b", user_text)
        tool_results: Dict[str, AgentToolResult] = {}

        transferish = any(
            w in lower for w in ("transfer", "send", "move", "wire", "pay")
        )
        if transferish:
            amt = self._transfer_amount(user_text, lower)
            if amt and len(nums) >= 2:
                tr = await self._execute_tool_call(
                    "process_transfer",
                    {
                        "amount": amt,
                        "from_account": nums[0],
                        "to_account": nums[1],
                    },
                )
                tool_results["t1"] = tr
                if tr.is_error or tr.result is None:
                    return (tr.error_message or "Transfer failed.", tool_results)
                return (str(tr.result), tool_results)
            return None

        balanceish = any(
            w in lower for w in ("balance", "how much", "funds", "money in")
        )
        if balanceish and nums:
            tr = await self._execute_tool_call("check_balance", {"account": nums[0]})
            tool_results["b1"] = tr
            if tr.is_error or tr.result is None:
                return (tr.error_message or "Balance lookup failed.", tool_results)
            return (str(tr.result), tool_results)

        infoish = any(
            w in lower
            for w in ("info", "details", "status", "type of account", "about account")
        )
        if infoish and nums:
            tr = await self._execute_tool_call(
                "get_account_info", {"account": nums[0]}
            )
            tool_results["i1"] = tr
            if tr.is_error or tr.result is None:
                return (tr.error_message or "Account info failed.", tool_results)
            return (str(tr.result), tool_results)

        if nums and not transferish:
            tr = await self._execute_tool_call("check_balance", {"account": nums[0]})
            tool_results["b1"] = tr
            if tr.is_error or tr.result is None:
                return (tr.error_message or "Balance lookup failed.", tool_results)
            return (str(tr.result), tool_results)

        return None

    @staticmethod
    def _transfer_amount(user_text: str, lower: str) -> Optional[str]:
        """Pick an amount that is unlikely to be a 4+ digit account number."""
        m = re.search(
            r"\$\s*(\d+(?:\.\d+)?)|(\d+(?:\.\d+)?)\s*(?:dollars?|usd|bucks)",
            user_text,
            re.I,
        )
        if m:
            return m.group(1) or m.group(2)
        tokens = re.findall(r"\b(\d+(?:\.\d+)?)\b", user_text)
        accounts = set(re.findall(r"\b\d{4,}\b", user_text))
        for t in tokens:
            if t in accounts:
                continue
            if "." in t:
                return t
            if len(t) <= 3:
                return t
        return None

    async def _text_only_reply(
        self, agent_input: AgentInput, system: str, user: str
    ) -> str:
        messages = [
            {KEY_ROLE: ROLE_SYSTEM, KEY_CONTENT: system},
            {KEY_ROLE: ROLE_USER, KEY_CONTENT: user},
        ]
        try:
            resp = LLMResponse.ensure_llm_response(
                await self.llm_client.acompletion(
                    messages,
                    metadata=self.get_llm_tracing_metadata(agent_input),
                )
            )
            if resp and resp.choices and len(resp.choices) >= 1:
                return resp.choices[0]
        except Exception:
            pass
        return user
