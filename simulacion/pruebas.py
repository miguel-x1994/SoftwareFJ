"""
Archivo: pruebas.py
Autor: Miguel Eduardo Jimenez Hidalgo
Descripcion: Este modulo contiene la simulacion de pruebas del sistema
Software FJ, incluyendo operaciones validas e invalidas para clientes,
servicios y reservas. Permite evidenciar el manejo de excepciones,
polimorfismo y funcionamiento general del sistema.

Fecha: 2026
"""

from modelos.cliente import Cliente
from modelos.servicios_especializados import *
from modelos.reserva import Reserva
from utilidades.logger import registrar_log


# Funcion principal de pruebas del sistema
def ejecutar_pruebas():

    # Lista para almacenar operaciones realizadas
    operaciones = []

    
    # CREACIoN DE CLIENTES
    
    try:

        cliente1 = Cliente(
            "Miguel",
            "migueljimenezh@unadvirtual.edu.co",
            "3104132601"
        )

        operaciones.append(cliente1)

    except Exception as e:
        registrar_log(str(e))

    try:

        # Cliente invalido (prueba de error)
        cliente2 = Cliente(
            "",
            "correo_malo",
            "abc"
        )

        operaciones.append(cliente2)

    except Exception as e:
        registrar_log(str(e))

    
    # RESERVA DE SALA (EXITOSA)
    
    try:

        sala = ReservaSala(
            "Sala Premium",
            100,
            20
        )

        reserva1 = Reserva(
            cliente1,
            sala,
            5
        )

        costo = reserva1.procesar()

        print("Costo:", costo)

    except Exception as e:
        registrar_log(str(e))

    
    # ALQUILER DE EQUIPO
    
    try:

        equipo = AlquilerEquipo(
            "Laptop Gamer",
            200,
            "Computador"
        )

        reserva3 = Reserva(
            cliente1,
            equipo,
            2
        )

        costo2 = reserva3.procesar()

        print("Costo alquiler:", costo2)

    except Exception as e:
        registrar_log(str(e))

    
    # ASESORiA ESPECIALIZADA
    
    try:

        asesoria = AsesoriaEspecializada(
            "Asesoria IA",
            300,
            "Carlos"
        )

        reserva4 = Reserva(
            cliente1,
            asesoria,
            3
        )

        costo3 = reserva4.procesar()

        print("Costo asesoria:", costo3)

    except Exception as e:
        registrar_log(str(e))

    
    # ERROR DE DURACIoN
    
    try:

        Reserva(cliente1, sala, 0)

    except Exception as e:
        registrar_log(str(e))

    
    # RESERVA CANCELADA
    
    try:

        reserva5 = Reserva(cliente1, sala, 1)

        reserva5.cancelar()

        print("Reserva cancelada")

        registrar_log("Reserva cancelada manualmente")

    except Exception as e:
        registrar_log(str(e))

    
    # POLIMORFISMO
    
    try:

        servicios = [sala, equipo, asesoria]

        for servicio in servicios:
            print(servicio.descripcion())

    except Exception as e:
        registrar_log(str(e))

    
    # RESERVA INVaLIDA
    
    try:

        reserva2 = Reserva(
            cliente1,
            sala,
            -5
        )

    except Exception as e:
        registrar_log(str(e))