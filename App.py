# app.py

from Validador import ValidadorUsuario
from Usuario import Usuario
from Errores import NombreInvalidoError, EdadInvalidaError, CorreoInvalidoError

class Aplicacion:
    def solicitar_datos(self):
        while True:
            try:
                nombre = input("Ingrese su nombre: ")
                edad = int(input("Ingrese su edad: "))
                correo = input("Ingrese su correo electrónico: ")

                ValidadorUsuario.validar(nombre, edad, correo)

                usuario = Usuario(nombre, edad, correo)
                print("\n" + str(usuario))
                break

            except NombreInvalidoError as e:
                print(f"x Error: {e}")
            except EdadInvalidaError as e:
                print(f"x Error: {e}")
            except CorreoInvalidoError as e:
                print(f"x Error: {e}")
            except ValueError:
                print("x Error: La edad debe ser un número entero.")
