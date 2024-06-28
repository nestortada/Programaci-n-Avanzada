# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:39:03 2023

@author: nesto
"""
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox
from Votacion import Ui_MainWindow
class AdmonVotacion(QMainWindow):

    def __init__(self):
        super(AdmonVotacion,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.PBtoro.clicked.connect(self.toro)
        self.ui.PBpuma.clicked.connect(self.puma)
        self.ui.PBardilla.clicked.connect(self.ardilla)
        self.ui.PBF.clicked.connect(self.ganador)
        self.ctoro=0
        self.cpuma =0
        self.cardilla =0
        
    def toro(self):
            self.ctoro=self.ctoro+1
            self.contador()
    def ardilla(self):
            self.cardilla=self.cardilla+1
            self.contador()
    def contador(self):
        total = self.cpuma+self.ctoro+self.cardilla
        self.ui.SBV.setValue(total)           
    def puma(self):
        self.cpuma=self.cpuma+1
        self.contador()
    def ganador(self):
        if self.cpuma == self.ctoro and self.ctoro == self.cardilla:
            QMessageBox.information(self, "Ganador", "Hubo un empate entre los tres")
        else:
            if self.cpuma < self.ctoro and self.ctoro == self.cardilla:
                QMessageBox.information(self, "Ganador", "Hubo un empate entre bruiesr y Jack")
            else:
                if self.cpuma < self.cardilla and self.ctoro < self.cardilla:
                    QMessageBox.information(self, "Ganador", "El ganador es Jack")
                else:
                    if self.cpuma == self.ctoro and self.ctoro > self.cardilla:
                        QMessageBox.information(self, "Ganador", "Hubo un empate entre Bernie y Bruiser")
                    else:
                        if  self.ctoro < self.cpuma and self.cpuma== self.cardilla:
                            QMessageBox.information(self, "Ganador", "Hubo un empate entre Bernie y Jack")
                        else:
                            if self.cpuma > self.ctoro and self.cpuma > self.cardilla:
                                QMessageBox.information(self, "Ganador", "El ganador es Bernie")
                            else:
                                if self.cpuma< self.ctoro and self.cardilla < self.ctoro:
                                    QMessageBox.information(self, "Ganador", "El ganador es Bruiser")
        self.close()    
if __name__ == '__main__':
    app = QApplication([])
    ventanaAdmonVotacion = AdmonVotacion()
    ventanaAdmonVotacion.show()
    sys.exit(app.exec())
