from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import load_data, save_data
import os

router = APIRouter(prefix="/api/profesores", tags=["Profesores"])

DATA_FILE = os.path.join("data", "profesores.json")

class Profesor(BaseModel):
    id: int | None = None
    nombre: str
    especialidad: str
    correo: str

@router.get("/")
def listar_profesores():
    return load_data(DATA_FILE)

@router.post("/")
def crear_profesor(profesor: Profesor):
    data = load_data(DATA_FILE)
    profesor.id = (max([p["id"] for p in data], default=0) + 1)
    data.append(profesor.dict())
    save_data(DATA_FILE, data)
    return profesor
