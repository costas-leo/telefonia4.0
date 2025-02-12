from domain.services.calculadora_costos import CalculadoraCostos
from domain.repositories.llamada_repository import LlamadaRepository

class FacturacionService:
    def __init__(self, llamada_repository: LlamadaRepository):
        self.llamada_repository = llamada_repository

    def calcular_gasto_usuario(self, telefono, fecha_inicio, fecha_fin):
        # Solo obtiene el costo total directamente desde el repositorio
        return self.llamada_repository.obtener_llamadas_por_usuario(telefono, fecha_inicio, fecha_fin)
