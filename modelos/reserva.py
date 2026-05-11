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
                "Duracion invalida. Debe ser mayor a 0"
            )

        # Atributos de la reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

   # Metodo para confirmar la reserva
    def confirmar(self):

    # Verificar estado
        if self.estado != "Pendiente":
            raise ReservaError(
            "Solo se pueden confirmar reservas pendientes."
        )

        self.estado = "Confirmada"

        registrar_log(
            "INFO",
            "Reserva confirmada correctamente"
    )

    # Metodo para cancelar la reserva
    def cancelar(self):
        
        #verificar si ya esta cancelada
        if self.estado == "Cancelada":
            raise ReservaError(
                "la reserva ya fue cancelada"
            )
        self.estado = "cancelada"
        
        registrar_log(
            "ATENCION",
            "Reserva cancelada"
        )

    # Metodo principal que procesa la reserva
    def procesar(self):

        try:
            
            #verificar estado antes de procesar
            if self.estado != "Confirmada":
                raise ReservaError(
                    "la reserva debe estar confirmada"
                )

            # Calcular costo del servicio
            costo = self.servicio.calcular_costo(
                self.duracion
            )
            
            # Registrar en logs
            registrar_log(
                "INFO",
                f"Reserva confirmada para {self.cliente.get_nombre()}"
            )
            
            #cambiar estado
            self.estado = "Procesada"
            
            return costo

        except Exception as e:

            # Cancelar reserva en caso de error
            self.cancelar()

            # Registrar error en logs
            registrar_log(
                "ERROR",
                f"Error procesando reserva: {str(e)}"
            )

            # Lanzar excepcion personalizada encadenada
            raise ReservaError(
                "No fue posible procesar la reserva"
            ) from e
    #Metodo para mostrar informacion
    def mostrar_info(self):
        
        return f"""
Cliente-: {self.cliente.get_nombre()}
Servicio: {self.servicio.get_nombre()}
Duracion: {self.duracion}
Estado: {self.estado}
""" 

    #Metod especal str
    def __str__(self):
        return self.mostrar_info()
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                         