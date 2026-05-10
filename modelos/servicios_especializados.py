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


# Clase que representa el servicio de reserva de salas
class ReservaSala(Servicio):

    def __init__(self, nombre, tarifa_base, capacidad):

        super().__init__(nombre, tarifa_base)
        self.capacidad = capacidad

    # Metodo para calcular el costo del servicio
    def calcular_costo(
        self,
        horas=1,
        descuento=0,
        impuesto=0
    ):
        subtotal = self.tarifa_base * horas

        subtotal -= subtotal * descuento

        subtotal += subtotal * impuesto

        return subtotal

    # Metodo que describe el servicio
    def descripcion(self):

        return f"""
Servicio: Reserva de Sala
Capacidad: {self.capacidad}
"""


# Clase que representa el servicio de alquiler de equipos
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, tarifa_base, tipo):

        super().__init__(nombre, tarifa_base)
        self.tipo = tipo

    # Metodo para calcular el costo del servicio
    def calcular_costo(self, dias=1):

        return self.tarifa_base * dias

    # Metodo que describe el servicio
    def descripcion(self):

        return f"""
Servicio: Alquiler de Equipo
Tipo: {self.tipo}
"""


# Clase que representa el servicio de asesoria especializada
class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, tarifa_base, especialista):

        super().__init__(nombre, tarifa_base)
        self.especialista = especialista

    # Metodo para calcular el costo del servicio
    def calcular_costo(self, horas=1):

        return self.tarifa_base * horas

    # Metodo que describe el servicio
    def descripcion(self):

        return f"""
Asesor: {self.especialista}
"""
