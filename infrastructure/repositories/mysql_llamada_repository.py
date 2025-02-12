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
            SELECT SUM(
                        CASE
                            WHEN llamadas.tipo = 'Internacional' THEN llamadas.duracion * 0.75
                            WHEN llamadas.tipo = 'Nacional' THEN 2.5
                            WHEN llamadas.tipo = 'Amigos' THEN
                                CASE
                                    WHEN amigos.amigos_count > 10 THEN 0
                                    ELSE 2.5
                                END
                            ELSE 0
                        END
                    ) AS costo_total
            FROM llamadas
            LEFT JOIN (
                SELECT numDeSalida, COUNT(*) AS amigos_count
                FROM llamadas
                WHERE tipo = 'Amigos'
                GROUP BY numDeSalida
            ) AS amigos ON llamadas.numDeSalida = amigos.numDeSalida
            WHERE llamadas.numDeSalida = %s
              AND llamadas.fecha BETWEEN %s AND %s;
        """
        cursor.execute(query, (telefono, fecha_inicio, fecha_fin))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()

        # Si el resultado existe, conviértelo en flotante para evitar el error
        return float(resultado['costo_total']) if resultado and resultado['costo_total'] is not None else 0.0
