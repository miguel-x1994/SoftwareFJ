"""
Archivo: entidad.py
Autor: Miguel Eduardo Jimenez Hidalgo
Descripcion: Clase abstracta base que representa una entidad general
dentro del sistema Software FJ. Define el metodo obligatorio

Fecha: 2026
"""

from abc import ABC, abstractmethod


# Clase abstracta base para todas las entidades del sistema
class Entidad(ABC):

    # Metodo abstracto obligatoro
    @abstractmethod
    def mostrar_info(self):
        pass
    
    #Metodo abstracto obligario para validar datos
    @abstractmethod
    def validar(self):
        pass
    
    #Metodo especial para mostar informa automatica
    def __str__(self):
        return self.mostrar_info()