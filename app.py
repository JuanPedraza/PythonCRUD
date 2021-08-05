# Traemos los imports y demás librerías que necesitemos
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys

# Cargamos la interfaz gráfica previamente creada en PYQT5-TOOLS DESIGNER

app = QtWidgets.QApplication([])
window = uic.loadUi("ventana.ui")
window.show()

sys.exit(app.exec())




