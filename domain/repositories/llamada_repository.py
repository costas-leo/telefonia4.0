from abc import ABC, abstractmethod

class LlamadaRepository(ABC):
    @abstractmethod
    def obtener_llamadas_por_usuario(self, telefono, fecha_inicio, fecha_fin):
        pass