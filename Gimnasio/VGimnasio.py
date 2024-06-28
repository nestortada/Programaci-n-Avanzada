# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 12:19:41 2023

@author: nesto
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from Gimnasio import Ui_MainWindow

class VGimnasio (QMainWindow):
    def __init__(self):
        super(VGimnasio, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.clicked.connect(self.boton_salir)
        
    def boton_salir(self):
        if self.ui.LN1.text() == "":
            QMessageBox.warning(self,"Falta nombre", "Debes poner tu nombre en la casilla de nombre")
        else:
            if self.ui.LN1_2.text() == "":
                QMessageBox.warning(self,"Falta apellido", "Debes poner tu apellido en la casilla de apellido")
            else:
                if not (self.ui.radioButton.isChecked() or self.ui.radioButton_2.isChecked() or self.ui.radioButton_3.isChecked()):
                    QMessageBox.warning(self, "Genero", "NO has seleccionado un genero!!!")
                else:
                    self.ui.pushButton.setEnabled(True)
                    QMessageBox.information(self, "Adios", "Ha sido resgistrado en  el gimnasio!!")
                    self.close()

if __name__ == "__main__":
    app = QApplication([])
    ventana = VGimnasio()
    ventana.show()
    sys.exit(app.exec())
    

        