from flask import Flask, render_template, url_for, redirect, request
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
    return render_template('layout.html', data=data)

#Ruta para eliminar un item de la lista
@app.route('/eliminar/<string:id>')
def eliminar(id):
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    c.execute(f'DELETE FROM articulos WHERE id = {id}')
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/agregar', methods=['GET','POST'])
def agregar():
    if request.method == 'GET':
        return render_template('stock.html')
    else:
        codigo = request.form['codigo']
        codInterno = request.form['codInterno']
        descripcion = request.form['descripcion']
        cantidad = request.form['cantidad']
        proveedor = request.form['proveedor']
        precio = request.form['precio']

        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        c.execute('INSERT INTO articulos (codigo, codinterno, descripcion, cantidad, proveedor, precio) VALUES (?,?,?,?,?,?)',(codigo, codInterno, descripcion, cantidad, proveedor, precio))
        conn.commit()
        conn.close()

    return redirect(url_for('index'))

@app.route('/editar/<id>', methods = ['POST', 'GET'])
def editar(id):
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM articulos WHERE id = {id}')
    articulo = c.fetchall()
    print(articulo)
    return render_template('stock.html', article = articulo[0])

@app.route('/actualizar/<id>', methods = ['POST', 'GET'])
def actualizar(id):
    if request.method == 'POST':
        codigo = request.form['codigo_edit']
        codInterno = request.form['codInterno_edit']
        descripcion = request.form['descripcion_edit']
        cantidad = request.form['cantidad_edit']
        proveedor = request.form['proveedor_edit']
        precio = request.form['precio_edit']
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        valores =  (codigo, codInterno, descripcion, cantidad, proveedor,precio,id)
        c.execute('UPDATE articulos SET codigo = ?, codinterno = ?,descripcion = ?,cantidad = ?,proveedor = ?,precio = ? WHERE id = ?', valores)
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
