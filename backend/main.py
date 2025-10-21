from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Configuración CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Base de datos temporal en memoria
profesores_db = []
cursos_db = []
comunicados_db = []

# Modelos Pydantic
class Profesor(BaseModel):
    id: Optional[str] = None
    nombre: str
    email: str
    asignatura: str

class Curso(BaseModel):
    id: Optional[str] = None
    nombre: str
    descripcion: Optional[str] = None

class Comunicado(BaseModel):
    id: Optional[str] = None
    titulo: str
    contenido: str

@app.get("/")
async def root():
    return {"message": "API Skoli funcionando correctamente"}

# CRUD Profesores
@app.get("/profesores")
async def get_profesores():
    return {"data": profesores_db}

@app.post("/profesores")
async def add_profesor(profesor: Profesor):
    profesores_db.append(profesor.dict())
    return {"data": "Profesor agregado", "profesor": profesor}

@app.put("/profesores/{profesor_id}")
async def update_profesor(profesor_id: str, profesor: Profesor):
    for i, p in enumerate(profesores_db):
        if p.get("id") == profesor_id:
            profesores_db[i] = profesor.dict()
            return {"data": "Profesor actualizado", "profesor": profesor}
    return {"error": "Profesor no encontrado"}

@app.delete("/profesores/{profesor_id}")
async def delete_profesor(profesor_id: str):
    for p in profesores_db:
        if p.get("id") == profesor_id:
            profesores_db.remove(p)
            return {"data": f"Profesor {profesor_id} eliminado"}
    return {"error": "Profesor no encontrado"}

# CRUD Cursos
@app.get("/cursos")
async def get_cursos():
    return {"data": cursos_db}

@app.post("/cursos")
async def add_curso(curso: Curso):
    cursos_db.append(curso.dict())
    return {"data": "Curso agregado", "curso": curso}

@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: str):
    for c in cursos_db:
        if c.get("id") == curso_id:
            cursos_db.remove(c)
            return {"data": f"Curso {curso_id} eliminado"}
    return {"error": "Curso no encontrado"}

# CRUD Comunicados
@app.get("/comunicados")
async def get_comunicados():
    return {"data": comunicados_db}

@app.post("/comunicados")
async def add_comunicado(comunicado: Comunicado):
    comunicados_db.append(comunicado.dict())
    return {"data": "Comunicado agregado", "comunicado": comunicado}

@app.delete("/comunicados/{comunicado_id}")
async def delete_comunicado(comunicado_id: str):
    for c in comunicados_db:
        if c.get("id") == comunicado_id:
            comunicados_db.remove(c)
            return {"data": f"Comunicado {comunicado_id} eliminado"}
    return {"error": "Comunicado no encontrado"}
