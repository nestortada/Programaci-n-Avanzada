
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from Convertidor import Ui_MainWindow

class Vconvertidor (QMainWindow):
    def __init__(self):
        super(Vconvertidor , self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.ui.PBSalir.setEnabled(False)
        self.ui.PBSalir.clicked.connect(self.boton_salir)
        self.ui.PBmm.clicked.connect(self.boton_mm)
        self.ui.PBcm.clicked.connect(self.boton_cm)
        self.ui.PBdm.clicked.connect(self.boton_dm)
        
    def boton_salir(self):
        QMessageBox.information(self, "Adios", "Esto se acabo!!")
        self.close()
        
    def boton_mm(self):
        
        if self.ui.SBmetros.value() == 0:
            QMessageBox.warning(self, "ERROR", "Y loss metros???")
        else:
            mm= self.ui.SBmetros.value()*1000
            self.ui.PBSalir.setEnabled(True)
            QMessageBox.information(self,"Resultado",str(self.ui.SBmetros.value()) + "metros es igual a" + str(mm)+ "mm")
    def boton_cm(self):
        if self.ui.SBmetros.value() == 0:
            QMessageBox.warning(self, "ERROR", "Y loss metros???")
        else:
            centi= self.ui.SBmetros.value()*100
            self.ui.PBSalir.setEnabled(True)
            QMessageBox.information(self,"Resultado",str(self.ui.SBmetros.value()) + "metros es igual a" + str(centi)+ "cm")
    def boton_dm(self):
        
        if self.ui.SBmetros.value() == 0:
            QMessageBox.warning(self, "ERROR", "Y loss metros???")
        else:
            dm= self.ui.SBmetros.value()*10
            self.ui.PBSalir.setEnabled(True)
            QMessageBox.information(self,"Resultado",str(self.ui.SBmetros.value()) + "metros es igual a" + str(dm)+ "dm")
if __name__ == "__main__":
    app = QApplication([])
    ventana = Vconvertidor()
    ventana.show()
    sys.exit(app.exec())
    

        