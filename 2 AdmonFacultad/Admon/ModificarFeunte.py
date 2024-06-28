# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:59:38 2023

@author: nesto
"""
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox

from Conex.Conexion import Conexion
from Diseno.DModificarFuente import Ui_MainWindow

class ModificarFuente(QMainWindow):
    def __init__(self):
        super(ModificarFuente, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.con = Conexion ()
        self.miConexion = self.con.conectar ()
        print('Objeto tipo AdmonFuentes creado y listo para usarse..!!')
        
        self.ui.pushButton.clicked.connect(self.ModificarFuente)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion )
        self.ui.PBSalir.setEnabled(True)
        self.ui.PBSalir.clicked.connect(self.boton_salir)
    def boton_salir(self):
        QMessageBox.information(self, "Adios", "Esto se acabo!!")
        self.close()

    def cerrarConexion(self):
        self.con.desconectar()
        self.close()
    def ModificarFuente(self):
        idFuenteOld = self.ui.SBCodigoViejo.value()
        if self.existeIdFuente(idFuenteOld) == False :
            QMessageBox.warning(self, "Error", "El codigo no existe ")
        else :
            idFuenteNew = self.ui.SBCodigoEliminar.value()
            if idFuenteNew != idFuenteOld and self.existeIdFuente(idFuenteNew) == True:
                QMessageBox.warning(self, "Error","Ya existe una fuente con ese ID, No se puede modificar")
            else:
                nombreNew=self.ui.NombreFuente.text()
                if nombreNew == "" :
                    QMessageBox.information(self, "Error", " lo dejaste en blanco")
                else:
                    contactoNew= self.ui.ContactoFuente.text()
                    BuscarContacto =self.BuscarContacto(idFuenteOld)
                    if contactoNew.lower() != BuscarContacto.lower() and (self.existeContacto(contactoNew)== True or contactoNew ==""):
                        QMessageBox.warning(self, "Error", "El contacto lo dejaste en blanco o ese contacto ya existe")
                    else:
                        try:
                            mycursor = self.miConexion.cursor()
                            mycursor.callproc('modFuente', [idFuenteNew, nombreNew, contactoNew, idFuenteOld])
                            self.miConexion.commit()
                            QMessageBox.information(self, "Modificacion exitosa",'La fuente ha sido modificada..!!')
                            mycursor.close()
                        except Exception as miError :
                            QMessageBox.warning(self, "Error en agregar", 'Fallo ejecutando el procedimiento')
                            print(miError)
                        self.close()
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
            
    def BuscarContacto(self,idFuente):
       try:
           mycursor = self.miConexion.cursor()
           mycursor.execute("SELECT contacto FROM fuentes WHERE idFuente = %s", (idFuente,))
           resultado=mycursor.fetchone()
           contacto = resultado[0]
           return contacto
       except Exception as miError:
           print('Fallo ejecutando el procedimiento')
           print(miError)

        
if __name__ == '__main__':
    app = QApplication([])
    ventanaAgregarFuentes = ModificarFuente()
    ventanaAgregarFuentes.show()
    sys.exit(app.exec())

        
        