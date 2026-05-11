"""
Archivo: servicios_especializados.py
Autor: Miguel Eduardo Jimenez Hidalgo
Descripcion: Este modulo contiene las clases que representan los servicios
especializados del sistema Software FJ. Estas clases heredan de la clase
abstracta Servicio e implementan sus metodos, demostrando herencia y
polimorfismo.

Fecha: 2026
"""

from modelos.servicio import Servicio
from excepciones.excepciones_personalizadas import (
    ServicioNoDisponibleError
)

# Clase que representa el servicio de reserva de salas
class ReservaSala(Servicio):

    def __init__(self, nombre, tarifa_base, capacidad):

        super().__init__(nombre, tarifa_base)
        
        # validar capacidad
        if capacidad <= 0:
            raise ServicioNoDisponibleError(
                "la capacidad debe ser mayor a 0"
            )
            
        self.capacidad = capacidad

    # Metodo para calcular el costo del servicio
    def calcular_costo(
        self,
        horas=1,
        descuento=0,
        impuesto=0
    ):
        
        #verificar disponibilidad
        self.verificar_disponibilidad()
        
        if horas <= 0:
            raise ServicioNoDisponibleError(
                "las horas deben ser mayores a 0"
            )
            
        subtotal = self.tarifa_base * horas

        subtotal -= subtotal * descuento

        subtotal += subtotal * impuesto

        return round (subtotal, 2)

    # Metodo que describe el servicio
    def descripcion(self):

        return f"""
Servicio: Reserva de Sala
Nombre: {self.nombre}
Capacidad: {self.capacidad}
tarifa base: ${self.tarifa_base}
"""
    #Metdo validad
    def validar(self):
        
        return self.capacidad > 0

# Clase que representa el servicio de alquiler de equipos
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, tarifa_base, tipo):

        super().__init__(nombre, tarifa_base)
        
        if tipo.strip() == "":
            raise ServicioNoDisponibleError(
                "El campo de equipo es obligatorio"
            )
            
        self.tipo = tipo.strip()

    # Metodo para calcular el costo del servicio
    def calcular_costo(self, dias=1):

        self.verificar_disponibilidad()
        
        if dias <=0:
            raise ServicioNoDisponibleError(
                "los dias deven ser mayores a 0"
            )
        return round(self.tarifa_base * dias, 2)

    # Metodo que describe el servicio
    def descripcion(self):

        return f"""
Servicio: Alquiler de Equipo
Nombre: {self.nombre}
Tipo: {self.tipo}
Tarifa base: ${self.tarifa_base}
"""

    #Metodo validar
    def validar(self):
        
        return self.tipo != ""
    
# Clase que representa el servicio de asesoria especializada
class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, tarifa_base, especialista):

        super().__init__(nombre, tarifa_base)
        
        if especialista.strip() == "":
            raise ServicioNoDisponibleError(
                "el nobmre del especialista es obligatorio"
            )
            
        self.especialista = especialista.strip()
        
    # Metodo para calcular el costo del servicio
    def calcular_costo(self, horas=1):
        
        self.verificar_disponibilidad()
        
        if horas <= 0:
            raise ServicioNoDisponibleError(
                "las horas debe ser mayores a 0"
            )

        return round(self.tarifa_base * horas, 2)

    # Metodo que describe el servicio
    def descripcion(self):

        return f"""
Servicio: Asesoria Especilista
Nombre: {self.nombre}
Assesor: {self.especialista}
Tarifa base: ${self.tarifa_base}
"""
    #metodo validar
    def validar(self):
        
        return self.especialista != ""