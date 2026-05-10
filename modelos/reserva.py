"""
Archivo: reserva.py
Autor: Miguel Eduardo Jimenez Hidalgo
Descripcion: Clase Reserva encargada de gestionar el proceso de creacion,
confirmacion y cancelacion de reservas dentro del sistema Software FJ.
Incluye validaciones, manejo de estados y control de errores mediante
excepciones personalizadas y registro en logs.

Fecha: 2026
"""

from excepciones.excepciones_personalizadas import *
from utilidades.logger import registrar_log


# Clase que representa una reserva en el sistema
class Reserva:

    # Constructor de la clase
    def __init__(self, cliente, servicio, duracion):

        # Validacion de duracion
        if duracion <= 0:
            raise DuracionInvalidaError(
                "Duracion invalida"
            )

        # Atributos de la reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # Metodo para confirmar la reserva
    def confirmar(self):
        self.estado = "Confirmada"

    # Metodo para cancelar la reserva
    def cancelar(self):
        self.estado = "Cancelada"

    # Metodo principal que procesa la reserva
    def procesar(self):

        try:

            # Calcular costo del servicio
            costo = self.servicio.calcular_costo(
                self.duracion
            )

            # Confirmar la reserva
            self.confirmar()

            # Registrar en logs
            registrar_log(
                f"Reserva confirmada para {self.cliente.mostrar_info()}"
            )

            return costo

        except Exception as e:

            # Cancelar reserva en caso de error
            self.cancelar()

            # Registrar error en logs
            registrar_log(
                f"Error procesando reserva: {str(e)}"
            )

            # Lanzar excepcion personalizada encadenada
            raise ReservaError(
                "No fue posible procesar la reserva"
            ) from e