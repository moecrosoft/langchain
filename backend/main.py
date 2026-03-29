from fastapi import FastAPI
from rag import generate_answer
from pydantic import BaseModel
from db import init_db

app = FastAPI()

init_db()

class AnalyseRequest(BaseModel):
    query: str

@app.post('/analyse')
async def analyse(data: AnalyseRequest):
    result = generate_answer(data.query)
    return result