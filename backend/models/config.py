from pydantic import BaseModel

class Config(BaseModel):
    tema: str
    nombre: str
    correo: str
    logo: str | None = None
