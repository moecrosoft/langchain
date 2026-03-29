from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from db import get_conn
import json
import re

embedding_model = HuggingFaceEmbeddings(
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'
)

llm = ChatOllama(
    model='llama3',
    base_url='http://ollama:11434'
    )

def extract_json(text):
    text = text.replace('```json', '').replace('```', '')

    match = re.search(r'\{.*\}', text, re.DOTALL)

    if not match:
        raise ValueError('No JSON found')
    
    return json.loads(match.group(0))

def search_similar(query):
    emb = embedding_model.embed_query(query)

    conn = get_conn()
    cur = conn.cursor()

    cur.execute('''
    SELECT content FROM incidents
    ORDER BY embedding <=> %s::vector
    LIMIT 3;
    ''', (emb, ))

    results = [r[0] for r in cur.fetchall()]

    cur.close()
    conn.close()

    return results

def generate_answer(query):
    context = search_similar(query)

    prompt = f'''
You are debugging a backend system.

Analyse the issue using the context provided.

User issue:
{query}

Similar incidents:
{chr(10).join(context)}

STRICT RULES:
- Output ONLY valid JSON
- No markdown
- No explanations
- No extra text before or after

Return format.

{{
    "root_cause": "string",
    "fix_steps": ["step1","step2"],
    "prevention": ["rule1","rule2"]
}}
'''
    
    response = llm.invoke(prompt).content

    try:
        return extract_json(response)
    except:
        return {
            'root_cause': 'Failed to parse response',
            'fix_steps': [response],
            'prevention': []
        }