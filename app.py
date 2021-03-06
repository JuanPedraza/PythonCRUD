# Traemos los imports y demás librerías que necesitemos
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import connect

# Validando los datos

def isEmpty():
    if window.txtNombre.text() == "" or window.txtCorreo.text() == "":
        alerta = QMessageBox()
        alerta.setText("¡No podemos almacenar datos vacíos!")
        # alerta.setIcon(QMessageBox.information)
        alerta.exec()
        return True


# Defininiendo las funciones CRUD de consulta

def agregar():
    if isEmpty():
        return False
    print("Soy el botón de agregar")
    nombre = window.txtNombre.text()
    correo = window.txtCorreo.text()
    print(nombre,correo)
    objContactos = connect.contactos()
    contactos = objContactos.createContactos((nombre,correo))
    consultar()
    
def modificar():
    if isEmpty():
        return False

    print("Soy el botón de modificar")
    id = window.txtID.text()
    nombre = window.txtNombre.text()
    correo = window.txtCorreo.text()
    objContactos = connect.contactos()
    contactos = objContactos.updateContactos((nombre,correo,id))
    consultar()

def eliminar():
    print("Soy el botón de eliminar")
    id = window.txtID.text()
    objContactos = connect.contactos()
    contactos = objContactos.deleteContactos(id)
    consultar()

def cancelar():
    print("Soy el botón de cancelar")
    consultar()


# Creamos una función para consultar los registros de la tabla

def consultar():
    window.tableContactos.setRowCount(0)
    indexControl = 0

    objContactos = connect.contactos()
    contactos = objContactos.readContactos()

    for contacto in contactos:
        window.tableContactos.setRowCount(indexControl+1)
        window.tableContactos.setItem(indexControl,0, QTableWidgetItem(str(contacto[0])))
        window.tableContactos.setItem(indexControl,1, QTableWidgetItem(str(contacto[1])))
        window.tableContactos.setItem(indexControl,2, QTableWidgetItem(str(contacto[2])))
        indexControl+=1

    # Limpiamos los campos
    window.txtID.setText("")
    window.txtNombre.setText("")
    window.txtCorreo.setText("")

    # Modificamos el comportamiento de los botones
    window.btnAgregar.setEnabled(True)
    window.btnModificar.setEnabled(False)
    window.btnEliminar.setEnabled(False)
    window.btnCancelar.setEnabled(False)

def seleccionar():
    id = window.tableContactos.selectedIndexes()[0].data()
    nombre = window.tableContactos.selectedIndexes()[1].data()
    correo = window.tableContactos.selectedIndexes()[2].data()
    print(id,nombre,correo)

    window.txtID.setText(id)
    window.txtNombre.setText(nombre)
    window.txtCorreo.setText(correo)

    # Modificamos el comportamiento de los botones
    window.btnAgregar.setEnabled(False)
    window.btnModificar.setEnabled(True)
    window.btnEliminar.setEnabled(True)
    window.btnCancelar.setEnabled(True)

# Cargamos la interfaz gráfica previamente creada en PYQT5-TOOLS DESIGNER

app = QtWidgets.QApplication([])
window = uic.loadUi("ventana.ui")
window.show()
consultar()

# Cambiando los nombres de las columnas de la tabla, que no sea editable y seleccione por fila
window.tableContactos.setHorizontalHeaderLabels(['ID','Nombre','Correo'])
window.tableContactos.setEditTriggers(QTableWidget.NoEditTriggers)
window.tableContactos.setSelectionBehavior(QTableWidget.SelectRows)

# Crear función para seleccionar los datos de la tabla
window.tableContactos.cellClicked.connect(seleccionar)


# Creando funciones para los botones

window.btnAgregar.clicked.connect(agregar)
window.btnModificar.clicked.connect(modificar)
window.btnEliminar.clicked.connect(eliminar)
window.btnCancelar.clicked.connect(cancelar)

sys.exit(app.exec())




