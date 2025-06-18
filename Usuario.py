# usuario.py

class Usuario:
    def __init__(self, nombre: str, edad: int, correo: str):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def __str__(self):
        return f"✔ Usuario válido:\n   Nombre: {self.nombre}\n   Edad: {self.edad}\n   Correo: {self.correo}"
