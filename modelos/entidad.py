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

    # Metodo abstracto que debe ser implementado por las clases hijas
    @abstractmethod
    def mostrar_info(self):
        pass