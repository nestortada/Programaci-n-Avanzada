# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:45:32 2023

@author: nesto
"""
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox

from Conex.Conexion import Conexion
from Diseno.DModificarDepartamento import Ui_MainWindow
class ModificarDepartamento(QMainWindow):
    def __init__(self):
        super(ModificarDepartamento,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.con = Conexion ()
        self.miConexion = self.con.conectar ()
        print('Objeto tipo AdmonFuentes creado y listo para usarse..!!')
        
        self.ui.pushButton.clicked.connect(self.modificarDepartamento)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion )
        self.ui.PBSalir.setEnabled(True)
        self.ui.PBSalir.clicked.connect(self.boton_salir)
    def boton_salir(self):
        QMessageBox.information(self, "Adios", "Esto se acabo!!")
        self.close()

    def cerrarConexion(self):
        self.con.desconectar()
        self.close()
        
    def modificarDepartamento(self):
        bandera=1
        idDepartamentoOld = self.ui.SBCodigoViejo.value()
        if self.existeidDepartamento(idDepartamentoOld)== False:
            QMessageBox.information(self, "EROR", "EL codigo no existe")
        else:
            idDepartamentoNew = self.ui.SBCodigoEliminar.value()
            if idDepartamentoNew!= idDepartamentoOld and self.existeidDepartamento(idDepartamentoNew) == True :
                QMessageBox.information(self, "Error", "El codigo ya existe")
            else :
                nombreNew=self.ui.NombreDepartamento.text()
                BuscarNombre= self.BuscarNombre(idDepartamentoOld)
                if nombreNew.lower() != BuscarNombre.lower() and (nombreNew == "" or self.existeNombre(nombreNew) == True) :
                    QMessageBox.information(self, "Error", " lo dejaste en blanco o ya existe el nombre en otro codigo")
                else:
                    if not self.ui.CBNEx.isChecked() and self.ui.ExtensionDepartamento.text() =="" :
                        QMessageBox.information(self, "Error", "No dijitaste nada en la extension y no marcaste la opcion de que no habia")
                    else:
                        extensionNew = self.ui.ExtensionDepartamento.text()
                        if self.ui.CBNEx.isChecked():
                            extensionNew = None
                        if self.ui.CBNJef.isChecked():
                            jefeNew= None
                        else:
                            jefeNew=self.ui.SBJefe.value()
                            if jefeNew!=self.BuscarJefe(idDepartamentoOld) and (self.existeJefe(jefeNew)== True or self.existeProfesor(jefeNew)==False):
                                QMessageBox.information(self, "Error", "El Jefe ya existe o no has creado un profesor con este codigo")
                                bandera =0   
                        if bandera !=0:
                            try : 
                                mycursor = self.miConexion.cursor ()
                                mycursor.callproc ("modDepartamento",[idDepartamentoNew,nombreNew,extensionNew,jefeNew,idDepartamentoOld])
                                self.miConexion.commit ()                
                                QMessageBox.information(self, "Modifiacción exitosa del departamento", "El departamento se ha modificado")
                                mycursor.close ()
                            except Exception as miError :
                                QMessageBox.warning(self, "ERROR en MODIFICAR",'Fallo ejecutando el procedimiento')
                                print(miError)
                                
    def existeidDepartamento (self,idDepartamento):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM DEPARTAMENTOS WHERE idDepartamento = %s"
            mycursor.execute(query, [idDepartamento])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)  
    def existeJefe(self,jefe):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM DEPARTAMENTOS WHERE JEFE = %s"
            mycursor.execute(query, [jefe])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)        
    def existeProfesor(self,idProfesor):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM PROFESORES WHERE IDPROFESOR = %s"
            mycursor.execute(query, [idProfesor])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
    def existeNombre(self,nombre):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM DEPARTAMENTOS WHERE NOMBRE = %s"
            mycursor.execute(query, [nombre])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
    def BuscarNombre(self,idDepartamento):
       try:
           mycursor = self.miConexion.cursor()
           mycursor.execute("SELECT nombre FROM departamentos WHERE idDepartamento = %s", (idDepartamento,))
           resultado=mycursor.fetchone()
           nombre = resultado[0]
           return nombre
       except Exception as miError:
           print('Fallo ejecutando el procedimiento')
           print(miError)
    def BuscarJefe(self,idDepartamento):
       try:
           mycursor = self.miConexion.cursor()
           mycursor.execute("SELECT jefe FROM departamentos WHERE idDepartamento = %s", (idDepartamento,))
           resultado=mycursor.fetchone()
           jefe = resultado[0]
           return jefe
       except Exception as miError:
           print('Fallo ejecutando el procedimiento')
           print(miError)
        
if __name__ == '__main__':
    app = QApplication([])
    ventanaAgregarFuentes = ModificarDepartamento()
    ventanaAgregarFuentes.show()
    sys.exit(app.exec())

