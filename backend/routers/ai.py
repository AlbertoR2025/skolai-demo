from fastapi import APIRouter
from pydantic import BaseModel
import openai

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/ask")
def ask_ai(data: Query):
    """
    Endpoint que recibe preguntas desde el front.
    Luego conectará con el modelo de IA (OpenAI, Ollama o Relevance).
    """
    question = data.question

    # Simulación de respuesta inicial
    fake_response = {
        "answer": f"Análisis generado para la pregunta: '{question}'",
        "suggestion": "En el futuro esta respuesta será generada por IA usando tus datos escolares."
    }

    return fake_response
