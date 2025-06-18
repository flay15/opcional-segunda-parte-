# validador.py

from Errores import NombreInvalidoError, EdadInvalidaError, CorreoInvalidoError

class ValidadorUsuario:
    @staticmethod
    def validar(nombre: str, edad: int, correo: str):
        if not nombre.replace(" ", "").isalpha():
            raise NombreInvalidoError("Nombre inválido. Solo debe contener letras y espacios.")

        if not (0 <= edad <= 120):
            raise EdadInvalidaError("Edad inválida. Debe estar entre 0 y 120.")

        if "@" not in correo or " " in correo:
            raise CorreoInvalidoError("Correo inválido. Debe contener '@' y no debe tener espacios.")
