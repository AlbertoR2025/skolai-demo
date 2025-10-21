from pydantic import BaseModel

class Comunicado(BaseModel):
    id: int
    titulo: str
    mensaje: str
    fecha: str
