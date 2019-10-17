from flask import Flask, render_template
import sqlite3
from sqlite3 import Error
import json

app = Flask(__name__)

## Función para conectarse con la base de datos de sqlite3.
## Comprobamos si existe algún problema con la conexión para lanzar
## un mensaje de error
def conexionDB():
    try:
        conn = sqlite3.connect("ejemplo.db")
    except Error as e:
        print('Se ha producido un error, ', e)
    return conn

## Función para desconectarse de la base de datos sqlite3
def desconexionDB(con):
    con.close()

## Muestra una página principal
@app.route("/")
def inicio():
    html = '<h1> Bienvenido a mi página </h1>'
    return html

## Muestra una lista con los nombres de las tablas que tenemos en la base de datos
@app.route("/html/tablas")
def listarTabla():
    conn = conexionDB()
    c = conn.cursor()
    res = []
    query = c.execute("select name from sqlite_master where type='table' and name not like 'sqlite_3';")
    for row in query:
        res.append(row)
    resFinal = json.dumps(res)
    desconexionDB(c)
    return render_template('tablas.html', name=res)

## Muestra una lista con los registros de una tabla en concreto
@app.route("/html/tablas/<string:t>")
def listarClientes(t):
    conn = conexionDB()
    c = conn.cursor()
    res = []
    query = c.execute("select * from " + t + " ;")
    for row in query:
        res.append(row)
    resFinal = json.dumps(res)
    desconexionDB(c)
    return render_template('tablas.html', name=res)

## Muestra una lista con los nombres de las columnas de una tabla y al final del
### todo aparece el número de registros que tiene dicha tabla
@app.route("/html/tablas/<string:t>/info")
def listarInfo(t):
    conn = conexionDB()
    c = conn.cursor()
    res = []
    query = c.execute("select * from " + t)
    for row in query.description:
        res.append(row[0])
    query2 = c.execute("select count(*) from " + t)
    for row in query2:
        res.append("numero de registros: " + str(row[0]))
    resFinal = json.dumps(res)
    desconexionDB(c)
    return render_template('tablas.html', name=res)

if __name__ == "__main__":
    app.run()
