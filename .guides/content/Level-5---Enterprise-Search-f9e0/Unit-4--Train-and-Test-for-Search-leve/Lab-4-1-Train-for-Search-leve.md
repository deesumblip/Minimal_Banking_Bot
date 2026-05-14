<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Train your agent to apply new search capabilities.

During training, `EnterpriseSearchPolicy` indexes the `.txt` files in `docs/` recursively. Because this course uses FAISS as the vector store, the resulting index is stored on disk locally. When the agent loads, that index is loaded into memory and used for retrieval. 

This on-disk and in-memory behaviour is specific to FAISS. If you were connecting to Milvus or Qdrant in production, indexing and retrieval would go through those external services instead.
 
Make sure `pattern_search` is overridden to call `action_trigger_search` before training, otherwise knowledge questions will not reach Enterprise Search.

## Step 1: Activate your virtual environment in the terminal

```bash
source .venv/bin/activate
```

## Step 2: Export OpenAI key
 
To make Enterprise Search Run, we added a new model group for OpenAI. Export it at the project root. 
 
```
echo 'OPENAI_API_KEY=your-openai-api-key' >> .env
```

## Step 2: Enter the Level 5 folder and train Rasa

 
```bash
cd level5
python -m rasa train
```
 
 {Check It!|assessment}(code-output-compare-2499735948)
