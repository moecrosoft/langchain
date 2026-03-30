from db import get_conn
from rag import embedding_model

data = [
    "Error: TimeoutError ollama Solution: increase timeout or preload model",
    "Error: connection refused postgres Solution: ensure container is running",
    "Error: FastAPI 500 error Solution: check logs and request validation",
    "Error: docker port already in use Solution: stop conflicting service",
    "Error: model not found ollama Solution: run ollama pull llama3",
    "Error: db connection failed Solution: verify POSTGRES_HOST",
    "Error: empty model response Solution: check prompt and model health",
    "Error: uvicorn failed Solution: check logs and port",
    "Error: slow inference Solution: optimize model or hardware",
    "Error: invalid JSON Solution: fix request format",
    "Error: permission denied postgres Solution: check credentials",
    "Error: service unavailable Solution: check container health",
    "Error: upload failed Solution: check file size/type",
    "Error: docker memory crash Solution: increase memory",
    "Error: pip install failed Solution: fix dependencies",
    "Error: frontend cannot reach backend Solution: check ports and CORS",
    "Error: GPU not detected Solution: check drivers",
    "Error: embedding mismatch Solution: use same embedding model",
    "Error: inference timeout Solution: increase timeout",
    "Error: database locked Solution: reduce concurrency",
    "Error: API not responding Solution: restart container",
    "Error: model loading slow Solution: preload model",
    "Error: wrong API endpoint Solution: check URL",
    "Error: SSL error Solution: check certificates",
    "Error: request blocked Solution: check firewall",
    "Error: incorrect environment variables Solution: verify .env",
    "Error: missing dependency Solution: install package",
    "Error: broken docker network Solution: restart network",
    "Error: high latency Solution: scale resources",
    "Error: invalid token Solution: refresh credentials"
]

def seed():
    conn = get_conn()
    cur = conn.cursor()

    for text in data:
        cur.execute(
            'SELECT 1 FROM incidents WHERE content = %s',
            (text,)
        )

        if cur.fetchone():
            continue

        emb = embedding_model.embed_query(text)

        cur.execute(
            'INSERT INTO incidents (content, embedding) VALUES (%s, %s)',
            (text, emb)
        )

    conn.commit()
    cur.close()
    conn.close()