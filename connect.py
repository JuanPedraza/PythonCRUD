# Librerías para conectar a la base de datos

import sqlite3
from sqlite3.dbapi2 import connect

# Creamos una clase cuyo método será realizar la conexión a la base de datos
# Se crean los distintos métodos que son los correspondientes al CRUD

class contactos:
    def iniciarConexion(self):
        conexion = sqlite3.connect('db.s3db')
        conexion.text_factory = lambda b: b.decode(errors = 'ignore')
        return conexion

    def readContactos(self):
        conexion = self.iniciarConexion()

        cursor = conexion.cursor()
        sentenciaSQL = "SELECT * FROM contactos"
        cursor.execute(sentenciaSQL)
        return cursor.fetchall()

    def createContactos(self,datosContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSQL = "INSERT INTO contactos (nombre,correo) VALUES(?,?)"
        cursor.execute(sentenciaSQL,datosContacto)
        conexion.commit()
        conexion.close()

    def deleteContactos(self,idContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSQL = "DELETE FROM contactos WHERE id=(?)"
        cursor.execute(sentenciaSQL,[idContacto])
        conexion.commit()
        conexion.close()


    def updateContactos(self,datosContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSQL = "UPDATE contactos SET nombre=?, correo=? WHERE id=?"
        cursor.execute(sentenciaSQL,datosContacto)
        conexion.commit()
        conexion.close()