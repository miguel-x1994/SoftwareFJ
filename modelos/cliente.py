"""
Archivo: cliente.py
Autor: Miguel Eduardo Jimenez Hidalgo
Descripcion: Clase Cliente que representa a los usuarios del sistema Software FJ.
Incluye validaciones de datos personales como nombre, correo y telefono,
aplicando encapsulacion y manejo de excepciones personalizadas.

Fecha: 2026
"""

from modelos.entidad import Entidad
from excepciones.excepciones_personalizadas import ClienteInvalidoError


# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    # Constructor de la clase
    def __init__(self, nombre, correo, telefono):

        # Atributos privados (encapsulacion)
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        # Validar datos al crear el objeto
        self.validar()

    # Metodo para validar los datos del cliente
    def validar(self):

        if len(self.__nombre.strip()) < 3:
            raise ClienteInvalidoError(
                "Nombre invalido"
            )

        if "@" not in self.__correo:
            raise ClienteInvalidoError(
                "Correo invalido"
            )

        if not self.__telefono.isdigit():
            raise ClienteInvalidoError(
                "Telefono invalido"
            )

    # Implementacion del metodo abstracto
    def mostrar_info(self):

        return f"""
Nombre: {self.__nombre}
Correo: {self.__correo}
Telefono: {self.__telefono}
"""