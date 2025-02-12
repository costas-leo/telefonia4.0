# Facturación Telefónica

Este proyecto es una aplicación backend desarrollada con **Python** y **Flask** para calcular los costos de facturación de usuarios basándose en su registro de llamadas. La aplicación interactúa con una base de datos **MySQL**, donde se almacenan los datos de usuarios y sus llamadas 

## Características

- Soporta tres tipos de llamadas: **Nacionales, Internacionales y Amigos**.
- Tarifas:
  - **Llamadas Nacionales:** $2.5 por llamada.
  - **Llamadas Internacionales:** $0.75 por segundo.
  - **Llamadas entre Amigos:** Gratuitas hasta 10 llamadas.
- Base de datos **MySQL** con tablas para usuarios, amigos, llamadas y boletas.
- API REST para calcular los costos de facturación de un usuario en un rango de fechas.

## Requisitos previos

- **Python 3.8+**
- **MySQL**
- **Postman** (opcional, para probar los endpoints)

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd costas-leo-telefonia4.0
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Unix/macOS:
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos MySQL

Asegúrate de tener MySQL instalado y en funcionamiento.

#### Crear la base de datos y tablas

Ejecuta el siguiente SQL en MySQL o usa el archivo `diseno_tablas.sql`:

```sql
CREATE DATABASE IF NOT EXISTS facturacion_telefonica;
USE facturacion_telefonica;
```

Luego, copia y ejecuta el contenido del archivo `diseno_tablas.sql`.

#### Insertar datos de prueba (opcional)

```bash
mysql -u root -p facturacion_telefonica < inserts_prueba.sql
```

### 5. Configurar la conexión a la base de datos

Edita las credenciales en `conexion.py`:

```python
conexion = {
    'host': 'localhost',
    'user': 'root',
    'password': '<TU_PASSWORD>',
    'database': 'facturacion_telefonica'
}
```

### 6. Ejecutar la aplicación

```bash
python main.py
```

La aplicación estará disponible en: [http://localhost:5000](http://localhost:5000)

## Uso

Para calcular el costo total de llamadas de un usuario en un rango de fechas, realiza una solicitud **POST** a:

```
http://localhost:5000/calcular_gastos
```
###  Ejemplo de solicitud en **Postman** o cURL:

```json
{
    "telefono": "+5491123456789",
    "fecha_inicio": "2025-01-01",
    "fecha_fin": "2025-01-31"
}
```

###  Ejemplo de respuesta esperada:

```json
{
    "costo_total": 457.5,
    "fecha_inicio": "2025-01-01",
    "fecha_fin": "2025-01-31",
    "telefono": "+5491123456789"
}
```

Este endpoint devuelve el **costo total** de las llamadas realizadas por el usuario en el período especificado.


