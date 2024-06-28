import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox,QTableWidgetItem

from Conex.Conexion import Conexion
from Diseno.DFuentes import Ui_MainWindow
from Admon.AgregarFuentes import AgregarFuentes
from Admon.ModificarFeunte import ModificarFuente

class AdmonFuentes(QMainWindow):

    def __init__(self):
        super(AdmonFuentes,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.con = Conexion ()
        self.miConexion = self.con.conectar ()
        print('Objeto tipo AdmonFuentes creado y listo para usarse..!!')
        
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
            mycursor.callproc ('allFuentes')
            
            a = self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)
                
                
            for result in mycursor.stored_results ():
                for (idFuente, nombre, contacto) in result :
                    self.ui.TWTabla.insertRow(cant)
                    
                    celdaCodigo = QTableWidgetItem(str(idFuente))
                    celdaNombre = QTableWidgetItem(nombre)
                    celdaContacto = QTableWidgetItem(contacto)
                    
                    self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                    self.ui.TWTabla.setItem(cant,1,celdaNombre)
                    self.ui.TWTabla.setItem(cant,2,celdaContacto)
                    
                    
                    cant = cant + 1
            if cant == 0 :
                QMessageBox.warning(self, "Alerta en Consulta", "No hay fuentes registradas")
            mycursor.close()
        except Exception as miError :
            QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Fuentes")
            print(miError)            

    def buscarFuente(self):
        idFuenteBuscar = self.ui.SBCodigoEliminar.value()
        if self.existeIdFuente(idFuenteBuscar) == False :
            QMessageBox.information(self, "Busqueda Fallida", "La fuente no existe, no se puede buscar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getFuente', [idFuenteBuscar])
    
                cant=0
                a = self.ui.TWTabla.rowCount()
                for rep in range(a):
                    self.ui.TWTabla.removeRow(0)
                    
                    
                for result in mycursor.stored_results ():
                    for (idFuente, nombre, contacto) in result :
                        self.ui.TWTabla.insertRow(cant)
                        
                        celdaCodigo = QTableWidgetItem(str(idFuente))
                        celdaNombre = QTableWidgetItem(nombre)
                        celdaContacto = QTableWidgetItem(contacto)
                        
                        self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                        self.ui.TWTabla.setItem(cant,1,celdaNombre)
                        self.ui.TWTabla.setItem(cant,2,celdaContacto)
                        
                        
                        cant = cant + 1
    
    
                mycursor.close()
    
            except Exception as miError :
                QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Fuentes")
                print(miError)  


    def agregaFuente(self):
        self.ventanaAgregarFuentes = AgregarFuentes()
        self.ventanaAgregarFuentes.show ()
        self.close()

    def eliminaFuente(self):
        idFuenteDel = self.ui.SBCodigoEliminar.value()
        if self.existeIdFuente ( idFuenteDel ) == False :
            QMessageBox.information(self, "Eliminacion Fallida", "La fuente no existe, no se puede eliminar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delFuente' , [ idFuenteDel ] )
                self.miConexion.commit()
                
                QMessageBox.information(self, "Eliminacion Exitosa", "La fuente ha sido eliminada")
                mycursor.close()
            except Exception as miError :
                QMessageBox.information(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Fuentes")
                print(miError)


    def modifyFuente(self):
        self.ventanaModificarFuente = ModificarFuente()
        self.ventanaModificarFuente.show ()
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

if __name__ == '__main__':
    app = QApplication([])
    ventanaAdmonFuentes = AdmonFuentes()
    ventanaAdmonFuentes.show()
    sys.exit(app.exec())
