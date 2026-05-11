"""
Archivo: excepciones_personalizadas.py
Autor: Miguel Eduardo Jimenez Hidalgo
Descripcion: Este archivo contiene las excepciones personalizadas
utilizadas en el sistema Software FJ para el manejo de errores.

Fecha: 2026
"""
# Excepcion base del sistema
class SofwareFJError(Exception):
    def __init__(self, mensaje,codigo="Error-000"):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.codigo = codigo
        
    def __str__(self):
        return f"[{self.codigo}] {self.mensaje}"
    
# Excepcion para errores en datos del cliente
class ClienteInvalidoError(SofwareFJError):
    def __init__(self, mensaje):
        super().__init__(mensaje, "Error-101")


# Excepcion para servicios no disponibles o incorrectos
class ServicioNoDisponibleError(SofwareFJError):
    def __init__(self, mensaje):
        super().__init__(mensaje, "Error-201")


# Excepcion general para errores en reservas
class ReservaError(SofwareFJError):
    def __init__(self, mensaje):
        super().__init__(mensaje, "Error-301")


# Excepcion para duracion invalida en reservas
class DuracionInvalidaError(SofwareFJError):
    def __init__(self, mensaje):
        super().__init__(mensaje, "Error-302")