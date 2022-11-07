from PySide2.QtWidgets import QPushButton, QApplication
from mainwindow import MainWindow
import sys

#Aplicación de QT
app = QApplication()
#Crear objeto
window = MainWindow()
#Hacer visible el elemento Botón
window.show()
#Qt loop
sys.exit(app.exec_())