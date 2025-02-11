from domain.services.calculadora_costos import CalculadoraCostos
from domain.repositories.llamada_repository import LlamadaRepository

class FacturacionService:
    def __init__(self, llamada_repository: LlamadaRepository):
        self.llamada_repository = llamada_repository

    def calcular_gasto_usuario(self, telefono, fecha_inicio, fecha_fin):
        llamadas = self.llamada_repository.obtener_llamadas_por_usuario(telefono, fecha_inicio, fecha_fin)
        costo_total = sum(CalculadoraCostos.calcular_costo_llamada(llamada) for llamada in llamadas)
        return round(costo_total, 2)