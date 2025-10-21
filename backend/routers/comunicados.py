from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import load_data, save_data

router = APIRouter(prefix="/api/comunicados", tags=["Comunicados"])

DATA_FILE = "data/comunicados.json"

class Comunicado(BaseModel):
    id: int | None = None
    titulo: str
    mensaje: str
    fecha: str

@router.get("/")
def listar_comunicados():
    return load_data(DATA_FILE)

@router.post("/")
def crear_comunicado(comunicado: Comunicado):
    comunicados = load_data(DATA_FILE)
    comunicado.id = len(comunicados) + 1
    comunicados.append(comunicado.dict())
    save_data(DATA_FILE, comunicados)
    return comunicado

@router.delete("/{comunicado_id}")
def eliminar_comunicado(comunicado_id: int):
    comunicados = load_data(DATA_FILE)
    comunicados = [c for c in comunicados if c["id"] != comunicado_id]
    save_data(DATA_FILE, comunicados)
    return {"message": "Comunicado eliminado correctamente"}
