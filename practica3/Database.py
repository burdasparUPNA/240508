import sqlite3

class Database:
    def __init__(self, nombreBD):
        self.nombre = nombreBD
        self.conexion = sqlite3.connect(self.nombre)
        self.cursor = self.conexion.cursor()

    def query(self, consulta):
        self.cursor.execute(consulta)

    def numeroResultados(self):
        return self.cursor.rowcount

    def getFirst(self):
        return self.cursor.fetchone()

    def getAll(self):
        return self.cursor.fetchall()

    def close(self):
        self.conexion.close()