from fastapi import FastAPI

from app.conversation import Conversation
from app.llm import LLM
from app.params import MODE

app = FastAPI()
llm = LLM()


@app.post("/intus/chatbot", response_model=Conversation)
def chat(chat: Conversation) -> Conversation:
    if MODE == "dev":
        return chat
    else:
        return Conversation(
            message=llm.llm_reponse(prompt=chat.message), session_name=chat.session_name
        )


@app.get("/")
def root():
    return {"message": "Hello World"}
