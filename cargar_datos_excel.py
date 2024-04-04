from openpyxl import *
import sqlite3
import pandas as pd

#BASE DATOS
conn = sqlite3.connect("stock.db")

cursor = conn.cursor()

crear = """CREATE TABLE articulos (id INTEGER PRIMARY KEY, codigo INTEGER, codinterno INTEGER, descripcion TEXT, cantidad INTEGER, tipo TEXT, proveedor TEXT, precio INTEGER)"""

df = pd.read_excel("stock.xlsx",sheet_name="Hoja1",decimal=".")
df["CODIGO"] = df["CODIGO"].fillna(0)

for index,row in df.iterrows():
    columna1 = str(row["CODIGO"])
    columna2 = str(row["DESCRIPCION"])
    columna3 = str(row["TIPO"])
    columna4 = int(row["PRECIO"])
    columna5 = int(row["CANT."])

    cursor.execute("""INSERT INTO articulos (codigo, codinterno, descripcion, cantidad, tipo, proveedor, precio) VALUES (?,?,?,?,?,?,?)""",(columna1,0,columna2,columna5,columna3,"nada",columna4))
conn.commit()
conn.close()

