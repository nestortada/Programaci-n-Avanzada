# Form implementation generated from reading ui file 'C:\Users\nesto\OneDrive - Universidad de la Sabana\AdmonCentroAdultos\Diseno\DCategoria.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdmonActividades(object):
    def setupUi(self, AdmonActividades):
        AdmonActividades.setObjectName("AdmonActividades")
        AdmonActividades.resize(1283, 646)
        self.centralwidget = QtWidgets.QWidget(parent=AdmonActividades)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 1181, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PBBuscar = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBBuscar.setFont(font)
        self.PBBuscar.setObjectName("PBBuscar")
        self.gridLayout.addWidget(self.PBBuscar, 4, 1, 1, 1)
        self.PBEliminar = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBEliminar.setFont(font)
        self.PBEliminar.setObjectName("PBEliminar")
        self.gridLayout.addWidget(self.PBEliminar, 3, 1, 1, 1)
        self.PBModificar = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBModificar.setFont(font)
        self.PBModificar.setObjectName("PBModificar")
        self.gridLayout.addWidget(self.PBModificar, 1, 2, 1, 1)
        self.LCodigoEliminar = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LCodigoEliminar.setFont(font)
        self.LCodigoEliminar.setObjectName("LCodigoEliminar")
        self.gridLayout.addWidget(self.LCodigoEliminar, 2, 0, 1, 2)
        self.PBSalir = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBSalir.setFont(font)
        self.PBSalir.setObjectName("PBSalir")
        self.gridLayout.addWidget(self.PBSalir, 6, 1, 1, 1)
        self.PBAgregar = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBAgregar.setFont(font)
        self.PBAgregar.setObjectName("PBAgregar")
        self.gridLayout.addWidget(self.PBAgregar, 1, 1, 1, 1)
        self.SBCodigoEliminar = QtWidgets.QSpinBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SBCodigoEliminar.setFont(font)
        self.SBCodigoEliminar.setMaximum(999999999)
        self.SBCodigoEliminar.setObjectName("SBCodigoEliminar")
        self.gridLayout.addWidget(self.SBCodigoEliminar, 3, 0, 1, 1)
        self.LTitulo = QtWidgets.QLabel(parent=self.layoutWidget)
        self.LTitulo.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LTitulo.setFont(font)
        self.LTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LTitulo.setObjectName("LTitulo")
        self.gridLayout.addWidget(self.LTitulo, 0, 0, 1, 3)
        self.PBTodas = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBTodas.setFont(font)
        self.PBTodas.setObjectName("PBTodas")
        self.gridLayout.addWidget(self.PBTodas, 3, 2, 1, 1)
        self.TWTabla = QtWidgets.QTableWidget(parent=self.layoutWidget)
        self.TWTabla.setMinimumSize(QtCore.QSize(711, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TWTabla.setFont(font)
        self.TWTabla.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.TWTabla.setObjectName("TWTabla")
        self.TWTabla.setColumnCount(6)
        self.TWTabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TWTabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWTabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWTabla.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWTabla.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWTabla.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWTabla.setHorizontalHeaderItem(5, item)
        self.TWTabla.horizontalHeader().setDefaultSectionSize(144)
        self.TWTabla.verticalHeader().setMinimumSectionSize(60)
        self.gridLayout.addWidget(self.TWTabla, 5, 0, 1, 3)
        AdmonActividades.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=AdmonActividades)
        self.statusbar.setObjectName("statusbar")
        AdmonActividades.setStatusBar(self.statusbar)

        self.retranslateUi(AdmonActividades)
        QtCore.QMetaObject.connectSlotsByName(AdmonActividades)
        AdmonActividades.setTabOrder(self.SBCodigoEliminar, self.PBEliminar)
        AdmonActividades.setTabOrder(self.PBEliminar, self.TWTabla)

    def retranslateUi(self, AdmonActividades):
        _translate = QtCore.QCoreApplication.translate
        AdmonActividades.setWindowTitle(_translate("AdmonActividades", "MainWindow"))
        self.PBBuscar.setText(_translate("AdmonActividades", "Buscar"))
        self.PBEliminar.setText(_translate("AdmonActividades", "Eliminar"))
        self.PBModificar.setText(_translate("AdmonActividades", "Modificar"))
        self.LCodigoEliminar.setText(_translate("AdmonActividades", "Código"))
        self.PBSalir.setText(_translate("AdmonActividades", "Salir"))
        self.PBAgregar.setText(_translate("AdmonActividades", "Agregar"))
        self.LTitulo.setText(_translate("AdmonActividades", "Administración de Actividades"))
        self.PBTodas.setText(_translate("AdmonActividades", "Ver Todas"))
        item = self.TWTabla.horizontalHeaderItem(0)
        item.setText(_translate("AdmonActividades", "Codigo"))
        item = self.TWTabla.horizontalHeaderItem(1)
        item.setText(_translate("AdmonActividades", "Nombre"))
        item = self.TWTabla.horizontalHeaderItem(2)
        item.setText(_translate("AdmonActividades", "Descripción"))
        item = self.TWTabla.horizontalHeaderItem(3)
        item.setText(_translate("AdmonActividades", "Fecha"))
        item = self.TWTabla.horizontalHeaderItem(4)
        item.setText(_translate("AdmonActividades", "IdCategoria"))
        item = self.TWTabla.horizontalHeaderItem(5)
        item.setText(_translate("AdmonActividades", "Centro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdmonActividades = QtWidgets.QMainWindow()
    ui = Ui_AdmonActividades()
    ui.setupUi(AdmonActividades)
    AdmonActividades.show()
    sys.exit(app.exec())