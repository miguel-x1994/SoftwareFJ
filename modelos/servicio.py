"""
Archivo: servicio.py
Autor: Miguel Eduardo Jimenez Hidalgo
Descripcion: Clase abstracta Servicio que representa los diferentes
tipos de servicios ofrecidos en el sistema Software FJ.
Define metodos abstractos que deben ser implementados por las clases
derivadas, como el calculo de costos y la descripcion del servicio.

Fecha: 2026
"""

from abc import ABC, abstractmethod


# Clase abstracta base para todos los servicios del sistema
class Servicio(ABC):

    # Constructor de la clase
    def __init__(self, nombre, tarifa_base):

        # Atributos del servicio
        self.nombre = nombre
        self.tarifa_base = tarifa_base

    # Metodo abstracto para calcular el costo del servicio
    @abstractmethod
    def calcular_costo(self):
        pass

    # Metodo abstracto para describir el servicio
    @abstractmethod
    def descripcion(self):
        pass