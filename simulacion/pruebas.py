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
    
    print("\n========================================")
    print("      SISTEMA SOFTWARE FJ")
    print("========================================\n")

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
        
        print("cliente registrado correctamente")

    except Exception as e:
        registrar_log(
            "Error",
            str(e)
        )

    try:

        # Cliente invalido (prueba de error)
        cliente2 = Cliente(
            "",
            "correo_malo",
            "abc"
        )

        operaciones.append(cliente2)

    except Exception as e:
        registrar_log(
            "Error",
            str(e)
        )

    
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
        #confirmar reserva antes de procesar
        reserva1.confirmar()
        
        costo = reserva1.procesar()

        print(f"Costo reserva sala: ${costo}")

    except Exception as e:
        registrar_log(
            "Error",
            str(e)
        )

    
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
        
        reserva3.confirmar()

        costo2 = reserva3.procesar()

        print(f"Costo alquiler: ${costo2}")

    except Exception as e:
        registrar_log(
            "Error",
            str(e)
        )

    
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

        reserva4 = Reserva(
            cliente1,
            asesoria,
            3
        )
        
        reserva4.confirmar()
        
        costo3 = reserva4.procesar()

        print("Costo asesoria: ${costo3}")

    except Exception as e:
        registrar_log(
            "Error",
            str(e)
        )

    
    # ERROR DE DURACIoN
    
    try:

        Reserva(cliente1, sala, 0)

    except Exception as e:
        
        registrar_log(
            "Error",
            str(e)
        )

    
    # RESERVA CANCELADA
    
    try:

        reserva5 = Reserva(
            cliente1,
            sala,
            1
        )

        reserva5.cancelar()

        print("Reserva cancelada")

        registrar_log(
            "Reserva cancelada manualmente"
        )

    except Exception as e:
        registrar_log(
            "Error",
            str(e)
        )

    
    # POLIMORFISMO
    
    try:

        servicios = [
            sala,
            equipo,
            asesoria
        ]
        
        print("\n=== SERVICIOS DISPONIBLES ===")

        for servicio in servicios:
            print(
                servicio.descripcion()
            )

    except Exception as e:
        registrar_log(
            "Error",
            str(e)
        )

    
    # RESERVA INVALIDA
    
    try:

        reserva2 = Reserva(
            cliente1,
            sala,
            -5
        )

    except Exception as e:
        registrar_log(
            "Error",
            str(e)
            
        )
        
    print("\n========================================")
    print("      FIN DE PRUEBAS")
    print("========================================")