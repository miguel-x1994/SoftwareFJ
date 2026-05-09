"""
Archivo: excepciones_personalizadas.py
Autor: Miguel Eduardo Jimenez Hidalgo
Descripcion: Este archivo contiene las excepciones personalizadas
utilizadas en el sistema Software FJ para el manejo de errores.

Fecha: 2026
"""

# Excepcion para errores en datos del cliente
class ClienteInvalidoError(Exception):
    pass


# Excepcion para servicios no disponibles o incorrectos
class ServicioNoDisponibleError(Exception):
    pass


# Excepcion general para errores en reservas
class ReservaError(Exception):
    pass


# Excepcion para duracion invalida en reservas
class DuracionInvalidaError(Exception):
    pass