from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Ruta para renderizar la plantilla HTML
@app.route('/')
def index():
    # Conectarse a la base de datos
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    
    # Ejecutar una consulta para obtener datos de la tabla
    c.execute('SELECT * FROM articulos')
    data = c.fetchall()
    
    # Cerrar la conexión
    conn.close()
    
    # Pasar los datos a la plantilla HTML y renderizarla
    return render_template('stock.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
