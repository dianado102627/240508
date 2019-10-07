from flask import Flask, render_template
import sqlite3
from sqlite3 import Error
import json

app = Flask(__name__)

def conexionDB():
    try:
        conn = sqlite3.connect("ejemplo.db")
    except Error as e:
        print('Se ha producido un error, ', e)
    return conn

def desconexionDB(con):
    con.close()

def listas(elementos):
    html = '<h1> Lista de elementos: </h1>'
    for i in elementos:
        html += '<ol>' + str(i) + '</ol>'
    return html


@app.route("/")
def listarTabla():
    conn = conexionDB()
    c = conn.cursor()
    res = []
    query = c.execute("select * from sqlite_master where type='table';")
    for row in query:
        res.append(row[1])
    resFinal = json.dumps(res)
    desconexionDB(c)
    html = listas(res)
    return html

@app.route("/Clientes")
def listarClientes():
    conn = conexionDB()
    c = conn.cursor()
    res = []
    query = c.execute("select * from Clientes;")
    for row in query:
        res.append(row[2])
    resFinal = json.dumps(res)
    desconexionDB(c)
    html = listas(res)
    return html

@app.route("/ids")
def listarIds():
    conn = conexionDB()
    c = conn.cursor()
    res = []
    query = c.execute("select IdCliente from Clientes;")
    for row in query:
        res.append(row[0])
    resFinal = json.dumps(res)
    desconexionDB(c)
    html = listas(res)
    return html

if __name__ == "__main__":
    app.run()
