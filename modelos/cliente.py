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
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

        # Validar datos al crear el objeto
        self.validar()

    # Metodo para validar los datos del cliente
    def validar(self):
        
        #validar nombre
        if len(self.__nombre) < 3:
            raise ClienteInvalidoError(
                "Nombre invalido. Minimo 3 caracteres."
            )
        # Validar Correo
        if "@" not in self.__correo or "." not in self.__correo:
            raise ClienteInvalidoError(
                "Correo invalido"
            )
        # Validar telefono
        if not self.__telefono.isdigit():
            raise ClienteInvalidoError(
                "Telefono invalido. Solo numeros"
            )
        return True
    
    # Metodo para mostar informacion del cliente
    def mostrar_info(self):

        return f"""
Nombre: {self.__nombre}
Correo: {self.__correo}
Telefono: {self.__telefono}
"""

    def get_nombre(self):
        return self.__nombre
    
    def get_correo(self):
        return self.__correo
    
    def get_telefono(self):
        return self.__telefono