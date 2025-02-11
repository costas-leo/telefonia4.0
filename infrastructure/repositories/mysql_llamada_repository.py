from domain.repositories.llamada_repository import LlamadaRepository
from domain.entities.llamada import Llamada
import mysql.connector

class MySqlLlamadaRepository(LlamadaRepository):
    def __init__(self, conexion):
        self.conexion = conexion

    def obtener_llamadas_por_usuario(self, telefono, fecha_inicio, fecha_fin):
        conn = mysql.connector.connect(**self.conexion)
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT * FROM llamadas
            WHERE numDeSalida = %s AND fecha BETWEEN %s AND %s;
        """
        cursor.execute(query, (telefono, fecha_inicio, fecha_fin))
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Llamada(**resultado) for resultado in resultados]