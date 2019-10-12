from flask import Flask, render_template, jsonify
from Database import Database
import re
app = Flask(__name__)

@app.route("/")
def getPrincipal():
    return render_template('plantillaPrincipal.html')

@app.route("/tables")
def getTablesJSON():
    salida = getTableNames()
    return jsonify(salida)

@app.route("/html/tables")
def getTables():
    salida = getTableNames()
    return render_template('plantillaTablas.html', lista = salida)

@app.route("/<tabla>")
def getTableJSON(tabla):
    salida = getDataOfTable(tabla)
    return jsonify(salida)

@app.route("/html/<tabla>")
def getTable(tabla):
    datosTabla = getDataOfTable(tabla)
    cabecerasTablas = getColumnNames(tabla)
    return render_template('plantillaTabla.html', nombre=tabla, cabecera=cabecerasTablas, tabla=datosTabla)

@app.route("/<tabla>/info")
def getTableInfoJSON(tabla):
    registros = getNumberRows(tabla)
    cabecerasTablas = getColumnNames(tabla)
    salida = {"registros":registros, "columnas":cabecerasTablas}
    return jsonify(salida)

@app.route("/html/<tabla>/info")
def getTableInfo(tabla):
    registros = getNumberRows(tabla)
    cabecerasTablas = getColumnNames(tabla)
    return render_template('plantillaInfo.html', nombre=tabla, cabecera=cabecerasTablas, elementos=registros)

def getColumnNames(tabla):
    db = getDB()
    db.query("select sql from sqlite_master where type='table' AND tbl_name = '" + tabla + "';")
    if db.numeroResultados() != 0:
        columnas = str(db.getFirst())
        columnas = columnas.split("`")
        salida = []
        # Los nombres de las columnas se encuentran en los puestos impares del array
        for i in range(0, len(columnas)):
            if i % 2 != 0:
                salida.append(columnas[i])
        # Eliminamos el primer elemento, corresponde al nombre de la tabla
        return salida[1:len(salida)]
    db.close()

def getTableNames():
    db = getDB()
    db.query("select name from sqlite_master where type='table' AND name NOT LIKE 'sqlite_%';")
    if db.numeroResultados() != 0:
        datos = db.getAll()
        salida = []
        for element in datos:
            salida.append(element[0])
    db.close()
    return salida

def getNumberRows(tabla):
    db = getDB()
    db.query("select count(*) from '" + tabla + "';")
    if db.numeroResultados() != 0:
        registros = str(db.getFirst())
    db.close()
    # Quitamos los caracteres que no nos interesan
    registros = registros.replace("(", "")
    registros = registros.replace(")", "")
    registros = registros.replace(",", "")
    return registros

def getDataOfTable(tabla):
    db = getDB()
    db.query("select * from '" + tabla + "';")
    if db.numeroResultados() != 0:
        datosTabla = db.getAll()
    db.close()
    return datosTabla

def getDB():
    return Database("ejemplo.db")

if __name__ == "__main__":
    app.run()
