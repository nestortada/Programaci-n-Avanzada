# -*- coding: utf-8 -*-
"""
Created on Sat May  6 19:27:00 2023

@author: nesto
"""
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox,QTableWidgetItem

from Conex.Conexion import Conexion
from Diseno.DDepartamento import Ui_MainWindow
from Admon.AgregarDepartamento import AgregarDepartamento
from Admon.ModificarDepartamento import ModificarDepartamento

class AdmonDepartamentos(QMainWindow):

    def __init__(self):
        super(AdmonDepartamentos,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.con = Conexion ()
        self.miConexion = self.con.conectar ()
        print('Objeto tipo AdmonDepartamentos creado y listo para usarse..!!')
        
        self.ui.PBTodas.clicked.connect(self.verTodas)
        self.ui.PBEliminar.clicked.connect(self.eliminaFuente )
        self.ui.PBBuscar.clicked.connect(self.buscarFuente)
        self.ui.PBAgregar.clicked.connect(self.agregaFuente)
        self.ui.PBModificar.clicked.connect(self.modifyFuente)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion )
        self.ui.PBSalir.setEnabled(True)
        self.ui.PBSalir.clicked.connect(self.boton_salir)
    def boton_salir(self):
        QMessageBox.information(self, "Adios", "Esto se acabo!!")
        self.close()

    def cerrarConexion(self):
        self.con.desconectar()
        self.close()

    def verTodas (self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor ()
            mycursor.callproc ('allDepartamentos')
            
            a = self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)
                
                
            for result in mycursor.stored_results ():
                for (iddepartamento, nombre, extension,jefe) in result :
                    self.ui.TWTabla.insertRow(cant)
                    
                    celdaCodigo = QTableWidgetItem(str(iddepartamento))
                    celdaNombre = QTableWidgetItem(nombre)
                    celdaExtension = QTableWidgetItem(extension)
                    celdaJefe = QTableWidgetItem(str(jefe))
                    
                    self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                    self.ui.TWTabla.setItem(cant,1,celdaNombre)
                    self.ui.TWTabla.setItem(cant,2,celdaExtension)
                    self.ui.TWTabla.setItem(cant,3,celdaJefe)
                    
                    
                    cant = cant + 1
            if cant == 0 :
                QMessageBox.warning(self, "Alerta en Consulta", "No hay Departamentos registradas")
            mycursor.close()
        except Exception as miError :
            QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de los Departamentos")
            print(miError)            
            
    def buscarFuente(self):
        idDepartamentoBuscar = self.ui.SBCodigoEliminar.value()
        if self.existeidDepartamento(idDepartamentoBuscar) == False:
            QMessageBox.information(self, "Búsqueda fallida", "El departamento no existe, no se puede buscar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getDepartamento', [idDepartamentoBuscar])
    
                a = self.ui.TWTabla.rowCount()
                for rep in range(a):
                    self.ui.TWTabla.removeRow(0)
    
                cant = 0
                for result in mycursor.stored_results():
                    for (idDepartamento, nombre, extension, jefe) in result:
                        self.ui.TWTabla.insertRow(cant)
    
                        celdaCodigo = QTableWidgetItem(str(idDepartamento))
                        celdaNombre = QTableWidgetItem(nombre)
                        celdaExtension = QTableWidgetItem(extension)
                        celdaJefe = QTableWidgetItem(str(jefe))
    
                        self.ui.TWTabla.setItem(cant, 0, celdaCodigo)
                        self.ui.TWTabla.setItem(cant, 1, celdaNombre)
                        self.ui.TWTabla.setItem(cant, 2, celdaExtension)
                        self.ui.TWTabla.setItem(cant, 3, celdaJefe)
    
                        cant += 1
    
                mycursor.close()
    
            except Exception as miError:
                QMessageBox.warning(self, "Consulta fallida", "Fallo ejecutando el procedimiento de consulta de los Departamentos")
                print(miError)
    
    def agregaFuente(self):
        self.ventanaAgregarDepartamento = AgregarDepartamento()
        self.ventanaAgregarDepartamento.show()
        self.close()
    
    def eliminaFuente(self):
        idDepartamentoDel = self.ui.SBCodigoEliminar.value()
        if self.existeidDepartamento( idDepartamentoDel ) == False :
            QMessageBox.information(self, "Eliminación fallida", "El departamento no existe, no se puede eliminar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delDepartamento', [idDepartamentoDel])
                self.miConexion.commit()
    
                QMessageBox.information(self, "Eliminación exitosa", "La fuente ha sido eliminada")
                mycursor.close()
            except Exception as miError:
                QMessageBox.information(self, "Consulta fallida", "Fallo ejecutando el procedimiento de consulta de las fuentes")
                print(miError)
    
    def modifyFuente(self):
        self.ventanaModificarDepartamento = ModificarDepartamento()
        self.ventanaModificarDepartamento.show()
        self.close()
    
    def existeidDepartamento(self, idDepartamento):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT COUNT(*) FROM DEPARTAMENTOS WHERE idDepartamento = %s"
            mycursor.execute(query, [idDepartamento])
            resultados = mycursor.fetchall()
            for registro in resultados:
                if registro[0] == 1:
                    return True
            return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)

if __name__ == '__main__':
    app = QApplication([])
    ventanaAdmonDepartamentos = AdmonDepartamentos()
    ventanaAdmonDepartamentos.show()
    sys.exit(app.exec())




    