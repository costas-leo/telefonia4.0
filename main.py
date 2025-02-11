from flask import Flask
from interfaces.controllers.facturacion_controller import calcular_gasto

app = Flask(__name__)
app.route('/calcular_gastos', methods=['POST'])(calcular_gasto)

if __name__ == '__main__':
    app.run(debug=True)