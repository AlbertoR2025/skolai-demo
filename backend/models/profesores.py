from pydantic import BaseModel

class Profesor(BaseModel):
    id: int
    nombre: str
    correo: str
    asignatura: str
