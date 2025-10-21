from fastapi import APIRouter
from pydantic import BaseModel
from database import load_data, save_data

router = APIRouter(prefix="/api/config", tags=["Configuración"])

DATA_FILE = "data/config.json"

class Config(BaseModel):
    tema: str
    nombre: str
    correo: str
    logo: str | None = None

@router.get("/")
def obtener_config():
    return load_data(DATA_FILE)

@router.post("/")
def guardar_config(config: Config):
    save_data(DATA_FILE, [config.dict()])
    return {"message": "Configuración guardada correctamente"}
