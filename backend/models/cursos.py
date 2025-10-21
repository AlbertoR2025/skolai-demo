from pydantic import BaseModel

class Curso(BaseModel):
    id: int
    nombre: str
    descripcion: str
    profesor: str
    activo: bool = True
