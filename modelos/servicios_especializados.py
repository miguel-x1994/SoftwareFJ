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

