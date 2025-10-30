from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    reply = f"echo: {req.message}"
    print(f"Received message: {req.message}, Replying with: {reply}")
    return {"reply": reply}