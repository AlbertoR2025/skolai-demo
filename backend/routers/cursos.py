from fastapi import APIRouter, HTTPException
import json, os

router = APIRouter(prefix="/api/cursos", tags=["Cursos"])

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "cursos.json")

# ✅ Cargar cursos
@router.get("/")
def listar_cursos():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# ✅ Crear curso
@router.post("/")
def crear_curso(curso: dict):
    try:
        # Cargar lista actual
        if os.path.exists(DATA_PATH):
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                cursos = json.load(f)
        else:
            cursos = []

        # Crear ID incremental
        nuevo_id = len(cursos) + 1
        curso["id"] = nuevo_id

        cursos.append(curso)

        # Guardar archivo
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(cursos, f, indent=4, ensure_ascii=False)

        return curso
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
