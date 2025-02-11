class CalculadoraCostos:
    @staticmethod
    def calcular_costo_llamada(llamada):
        if llamada.tipo == "Nacional":
            return 2.5
        elif llamada.tipo == "Internacional":
            return llamada.duracion * 0.75
        elif llamada.tipo == "Amigos":
            return 0  # Gratis hasta 10 llamadas
        else:
            return 0