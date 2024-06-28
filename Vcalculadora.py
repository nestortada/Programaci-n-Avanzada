import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from Calculadora import Ui_MainWindow

class Vcalculadora (QMainWindow):
    def __init__(self):
        super(Vcalculadora , self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.ui.PBSalir.setEnabled(True)
        self.ui.PBSalir.clicked.connect(self.boton_salir)
        self.ui.PBSuma.clicked.connect(self.boton_suma)
        self.ui.PBResta.clicked.connect(self.boton_resta)
        self.ui.PBMultiplicacion.clicked.connect(self.boton_multi)
        self.ui.PBDivision.clicked.connect(self.boton_division)
        self.ui.PBFactorial.clicked.connect(self.boton_fact)
        
    def boton_salir(self):
        QMessageBox.information(self, "Adios", "Esto se acabo!!")
        self.close()
        
    def boton_suma(self):
            suma= self.ui.SBOperando1.value() + self.ui.SBOperando2.value()
            self.ui.PBSalir.setEnabled(True)
            self.ui.SBResultado.setValue(suma)
    def boton_resta(self):
        resta= self.ui.SBOperando1.value() - self.ui.SBOperando2.value()
        self.ui.PBSalir.setEnabled(True)
        self.ui.SBResultado.setValue(resta)
    def boton_multi(self):
        multi= self.ui.SBOperando1.value() * self.ui.SBOperando2.value()
        self.ui.PBSalir.setEnabled(True)
        self.ui.SBResultado.setValue(multi)
    def boton_division(self):
        if self.ui.SBOperando2.value()==0:
            QMessageBox.warning(self, "ERROR", "No puedes dividir por 0")
        else:
            division= self.ui.SBOperando1.value() // self.ui.SBOperando2.value()
            self.ui.PBSalir.setEnabled(True)
            self.ui.SBResultado.setValue(division)
    def boton_fact(self):
        if self.ui.SBOperando1.value()<0:
            QMessageBox.warning(self, "ERROR", "El primer operador debe ser mayor o igual a 0")
        else:
            if self.ui.SBOperando1.value() == 0:
                self.ui.SBResultado.setValue(1)
            else:
                if self.ui.SBOperando1.value()>9:
                    cont=0
                    mult=1
                    for rep in range(self.ui.SBOperando1.value()):
                        cont=cont+1
                        mult=cont*mult
                    QMessageBox.information(self, "Resultado", "El factorial de "+str(self.ui.SBOperando1.value())+" es " + str(mult))
                else:
                    cont=0
                    mult=1
                    for rep in range(self.ui.SBOperando1.value()):
                        cont=cont+1
                        mult=cont*mult
                    self.ui.SBResultado.setValue(mult)
                    
if __name__ == "__main__":
    app = QApplication([])
    ventana = Vcalculadora()
    ventana.show()
    sys.exit(app.exec())
    

        