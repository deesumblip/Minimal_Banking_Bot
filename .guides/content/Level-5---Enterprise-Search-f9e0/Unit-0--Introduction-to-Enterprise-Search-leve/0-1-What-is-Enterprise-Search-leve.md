This chapter adds enterprise search to your banking agent using retrieval-augmented generation (RAG).
 
With RAG, the agent:
 
1\. Searches documents for relevant information  
2\. Uses an LLM to generate an answer based on what it finds
 
When you use RAG, you can delegate FAQ questions like "What is the fee for international transfers?" using your existing documents instead of hard coding every response.
 
In Rasa, this is done with the `EnterpriseSearchPolicy`. You store knowledge in .txt files, Rasa indexes them during training, and at runtime the agent retrieves content and generates an answer, no new flows or responses needed. 