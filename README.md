# 💻 Debug Assistant AI

An end-to-end AI system that analyzes system errors and logs, retrieves similar past incidents using vector search, and generates root cause analysis with suggested fixes using large language models. This project combines Retrieval-Augmented Generation (RAG), FastAPI, PostgreSQL with pgvector, a Streamlit frontend, and full Dockerized deployment.

---

## 📌 Overview

Users can:

- Input system errors, logs, or failure messages
- Retrieve similar past incidents using semantic search
- Get AI-generated root cause analysis and solutions
- Understand how to fix and prevent issues
- Interact with the system via a simple UI

---

## 🧠 How It Works

1. **Input** — User enters an error or issue via Streamlit UI
2. **Send** — Frontend sends query to backend via `POST /analyze`
3. **Embedding** — Query is converted into a vector using a sentence transformer model
4. **Retrieval** — PostgreSQL (pgvector) finds similar past incidents
5. **Augmentation** — Retrieved context is combined with the user query
6. **Generation** — LLaMA 3 (via Ollama) generates root cause and solution
7. **Return** — Response is sent back and displayed in the UI

---

## 🏗️ Tech Stack

| Layer     | Technology                                      |
|-----------|-------------------------------------------------|
| Backend   | FastAPI, LangChain, psycopg2                    |
| AI Models | sentence-transformers (embeddings), LLaMA 3 (Ollama) |
| Frontend  | Streamlit                                       |
| Database  | PostgreSQL + pgvector                           |
| DevOps    | Docker, Docker Compose                          |

---

## 📂 Project Structure
```
incident_ai/
│
├── backend/
│   ├── main.py
│   ├── rag.py
│   ├── db.py
│   ├── seed.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── docker-compose.yml
└── README.md
```

---

## 🚀 Getting Started
```bash
git clone https://github.com/your-username/incident_ai.git
cd incident_ai
docker-compose up -d --build
```

This starts:

- **Frontend** → http://localhost:8501
- **Backend** → http://localhost:8000
- **PostgreSQL (pgvector)** → running in container
- **Ollama (LLaMA 3)** → running in container

---

## 🔗 API Reference

### `POST /analyze`

**Request:**
```json
{
  "query": "TimeoutError while calling Ollama model"
}
```

**Response:**
```json
{
  "response": "Root cause: The model is not fully loaded or request timed out...\nFix: Increase timeout or preload model...\nPrevention: Ensure model is ready before requests."
}
```

---

## 🤖 Model Details

| Component       | Value                                        |
|-----------------|----------------------------------------------|
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2       |
| LLM             | LLaMA 3 (via Ollama)                         |
| Input           | Error logs / system messages                 |
| Output          | Root cause + fix + prevention                |
| Framework       | LangChain                                    |
| Strategy        | RAG (Retrieval-Augmented Generation)         |

---

## 📊 RAG Pipeline
```
User Query
→ Embedding (vector)
→ pgvector similarity search
→ Retrieve top-k incidents
→ Inject into prompt
→ LLM generates solution
```

---

## 🎯 Features

- ✅ Semantic error search using embeddings
- ✅ pgvector-powered similarity retrieval
- ✅ LangChain-based LLM orchestration
- ✅ Root cause + fix + prevention generation
- ✅ Streamlit UI for interaction
- ✅ Dockerized microservices architecture
- ✅ Real-world debugging use case

---

## 💡 Example Use Case

**Input:**
```
Request timeout while calling LLaMA 3 via FastAPI
```

**Output:**
```
Root cause: Model not ready or timeout threshold too low
Fix: Increase timeout or preload model using ollama pull
Prevention: Implement health checks before inference calls
```

---

## 🚀 Future Improvements

- [ ] Add conversation memory (multi-turn debugging)
- [ ] Integrate LangGraph for multi-step reasoning
- [ ] Expand dataset with real-world incidents
- [ ] Add confidence scoring
- [ ] Deploy on AWS EC2 with CI/CD

---

## 🏁 Summary

This project demonstrates how to build a production-style AI system that combines:

- **Retrieval** (pgvector)
- **Reasoning** (LLM)
- **Orchestration** (LangChain)

to solve real-world engineering problems like debugging and incident analysis.