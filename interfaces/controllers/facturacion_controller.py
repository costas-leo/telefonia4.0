from flask import request, jsonify
from application.services.facturacion_service import FacturacionService
from infrastructure.repositories.mysql_llamada_repository import MySqlLlamadaRepository
from infrastructure.database.conexion import Conexion

def calcular_gasto():
    try:
        data = request.json
        telefono = data.get('telefono')
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')

        if not telefono or not fecha_inicio or not fecha_fin:
            return jsonify({'error': 'Faltan datos obligatorios'}), 400

        conexion = Conexion.obtener_conexion()
        llamada_repository = MySqlLlamadaRepository(conexion)
        facturacion_service = FacturacionService(llamada_repository)

        costo_total = facturacion_service.calcular_gasto_usuario(telefono, fecha_inicio, fecha_fin)

        # Aquí generarías la boleta con el costo total calculado
        boleta = {
            'telefono': telefono,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'costo_total': costo_total
        }

        return jsonify(boleta)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
