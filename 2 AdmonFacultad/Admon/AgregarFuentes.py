# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:10:10 2023

@author: nesto
"""
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox

from Conex.Conexion import Conexion
from Diseno.DAgregarFuentes import Ui_MainWindow
class AgregarFuentes(QMainWindow):
    def __init__(self):
        super(AgregarFuentes,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.con = Conexion ()
        self.miConexion = self.con.conectar ()
        print('Objeto tipo AdmonFuentes creado y listo para usarse..!!')
        
        self.ui.PBAgregar.clicked.connect(self.AgregarFuente)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion )
        self.ui.PBSalir.setEnabled(True)
        self.ui.PBSalir.clicked.connect(self.boton_salir)
    def boton_salir(self):
        QMessageBox.information(self, "Adios", "Esto se acabo!!")
        self.close()

    def cerrarConexion(self):
        self.con.desconectar()
        self.close()
        
    def AgregarFuente(self):
        idFuenteNew = self.ui.SBCodigoEliminar.value()
        if self.existeIdFuente(idFuenteNew) == True :
            QMessageBox.information(self, "Error", "El codigo ya existe")
        else :
           nombreNew=self.ui.NombreFuente.text()
           if nombreNew == "" :
               QMessageBox.information(self, "Error", " lo dejaste en blanco el nombre")
           else:
               contactoNew= self.ui.ContactoFuente.text()
               if self.existeContacto(contactoNew)== True or contactoNew =="":
                   QMessageBox.information(self, "Error", "El contacto lo dejaste en blanco o ese contacto ya existe")
               else:
                   try : 
                       mycursor = self.miConexion.cursor ()
                       mycursor.callproc ("newFuente",[idFuenteNew,nombreNew,contactoNew])
                       self.miConexion.commit ()                
                       QMessageBox.information(self, "Creacion exitosa de la fuente", "La fuente ha sido creada")
                       mycursor.close ()
                   except Exception as miError :
                       QMessageBox.warning(self, "ERROr en agregar",'Fallo ejecutando el procedimiento')
                       print(miError)
    def existeIdFuente (self,idFuente):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM FUENTES WHERE idFuente = %s"
            mycursor.execute(query, [idFuente])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)  
    def existeContacto (self,Contacto):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM FUENTES WHERE Contacto = %s"
            mycursor.execute(query, [Contacto])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
    
if __name__ == '__main__':
    app = QApplication([])
    ventanaAgregarFuentes = AgregarFuentes()
    ventanaAgregarFuentes.show()
    sys.exit(app.exec())

