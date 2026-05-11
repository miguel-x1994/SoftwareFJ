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
from excepciones.excepciones_personalizadas import (
    ServicioNoDisponibleError
)

# Clase abstracta base para todos los servicios del sistema
class Servicio(ABC):

    # Constructor de la clase
    def __init__(self, nombre, tarifa_base):
        
        #validacion de tarifa
        if tarifa_base <= 0:
            raise ServicioNoDisponibleError(
                "ka tarifa base debe ser mayor a 0"
            )

        # Atributos del servicio
        self.nombre = nombre.strip()
        self.tarifa_base = tarifa_base
        self.disponible = True
    
    # Metod para verificar disponibilidad
    def verificar_disponibilidad(self):
        
        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.nombre} no esta disponible"
            )

    # Metodo abstracto para calcular el costo del servicio
    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    # Metodo abstracto para describir el servicio
    @abstractmethod
    def descripcion(self):
        pass
    
    # Metodo para mostar informacion
    def mostar_info(self):
        
        estado = "Disponible" if self.disponible else "No disponible"
        
        return f"""
    
    Servicio: {self.nombre}
    Tarifa base: ${self.tarifa_base}
    Estado: {estado}
    """
    
        # Metodo para validar datos
        def validar(self):
            
            return (
                self.nombre != ""
                and self.tarifa_base > 0
            )
            
        # Metodo especial str
        def __str__(self):
            
            return self.mostar_info()
        
        def get_nombre(self):
            return self.nombre
            
        def get_tarifa_base(self):
            return self.tarifa_base