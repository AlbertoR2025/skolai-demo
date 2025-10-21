from fastapi import APIRouter
import json, os

router = APIRouter(prefix="/api/resumen", tags=["Resumen"])

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def contar_registros(archivo):
    path = os.path.join(BASE_DIR, archivo)
    if not os.path.exists(path):
        return 0
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return len(data)

@router.get("/")
def obtener_resumen():
    return {
        "profesores": contar_registros("profesores.json"),
        "cursos": contar_registros("cursos.json"),
        "comunicados": contar_registros("comunicados.json")
    }
