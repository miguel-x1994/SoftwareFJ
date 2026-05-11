"""
Archivo: main.py
Autor: Miguel Eduardo Jimenez Hidalgo
Descripcion: Archivo principal del sistema Software FJ. Inicia la ejecucion del programa, mostrando la interfaz en consola
y llamando al modulo de pruebas para simular el funcionamiento del sistema.

Fecha: 2026
"""

from simulacion.pruebas import ejecutar_pruebas


# Mensaje de bienvenida del sistema
print("""
=================================
=           SOFTWARE FJ         =
=      Sistema de Reservas      =
=================================
""")


# Ejecucion de pruebas del sistema
ejecutar_pruebas()


# Mensaje final del sistema
print("""
Sistema ejecutado correctamente
aunque existieron errores.
""")