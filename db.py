import sqlite3

conn = sqlite3.connect("stock.db")
cursor = conn.cursor()
crear = """CREATE TABLE IF NOT EXISTS pruebas (id INTEGER PRIMARY KEY, codigo INTEGER, codinterno INTEGER,
 descripcion TEXT, cantidad INTEGER, tipo TEXT, proveedor TEXT, precio REAL,
 CHECK (typeof(codigo)="integer" AND typeof(codinterno)="integer" AND typeof(descripcion)="text" 
 AND typeof(cantidad)="integer" AND typeof(tipo)="text" AND typeof(proveedor)="text" AND typeof(precio)="real"))"""

print("Base de Datos iniciada...")




def AñadirDato(codigo, codinterno, descripcion, cantidad, tipo, proveedor, precio):
    try:
        cursor.execute(f"""INSERT INTO pruebas (codigo,codinterno,descripcion,cantidad,tipo,proveedor,precio) VALUES ({codigo},{codinterno},{descripcion},{cantidad},{tipo},{proveedor},{precio})""")
        conn.commit()
        print("Datos cargados con éxito...")
        return True 
    except sqlite3.IntegrityError as error:
        print("Error al cargar los datos: ", error)
        return False



def LeerDatos():
    cursor.execute("""SELECT * FROM pruebas""")
    datos = cursor.fetchall()
    for i in datos: 
        print(i)

def LeerDato(columna, dato):
        cursor.execute(f"""SELECT * FROM pruebas WHERE {columna} = {dato}""")
        dato = cursor.fetchone()
        if dato:
            print("Articulo encontrado")
            print("Codigo: ",dato[1])
            print("Código Interno:", dato[2])
            print("Descripción:", dato[3])
            print("Cantidad:", dato[4])
            print("Tipo:", dato[5])
            print("Proveedor:", dato[6])
            print("Precio:", dato[7])
        else:
            print("Dato no encontrado")

def EditarDato(columna, dato , dato_actualizado): 
    try:
        cursor.execute(f"""UPDATE pruebas SET {columna} = {dato_actualizado} WHERE {columna} = {dato}""")
        conn.commit()
        return True, print("Dato actualizado con exito")
    except sqlite3.OperationalError as error:
        print("No se pudo actualizar el dato, comprueba que el tipo de dato sea correcto")
        return False
    
def EliminarDato(columna,dato): 
    cursor.execute(f"""DELETE FROM pruebas WHERE {columna} = {dato}""")
    conn.commit()
    print("Articulo eliminado con exito")


# resultado = AñadirD   ato(2,1,"Hola",1,"FABIMAG","BENVENUTO",100)

# if resultado: 
#     print("El dato esta guardado")

# else: 
#     print("Hubo un error al cargar los datos")

