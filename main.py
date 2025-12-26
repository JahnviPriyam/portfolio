from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Contact Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactMessage(BaseModel):
    name: str
    email: str
    message: str

messages = []

@app.post("/contact")
def send_message(msg: ContactMessage):
    messages.append(msg)
    return {"status": "success", "message": "Message received"}

@app.get("/health")
def health():
    return {"status": "running"}
