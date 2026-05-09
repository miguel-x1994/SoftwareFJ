"""
Archivo: logger.py
Autor: Miguel Eduardo Jimenez Hidalgo
Descripcion: Este modulo se encarga de registrar eventos y errores
del sistema Software FJ en un archivo de logs.txt, incluyendo fecha y hora.

Fecha: 2026
"""

from datetime import datetime


# Funcion para registrar mensajes en el archivo de logs
def registrar_log(mensaje):

    # Obtener fecha y hora actual formateada
    fecha = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Crear archivo logs.txt en modo agregar
    with open(
        "logs.txt",
        "a",
        encoding="utf-8"
    ) as archivo:

        # Escribir mensaje con fecha en el archivo
        archivo.write(
            f"[{fecha}] {mensaje}\n"
        )