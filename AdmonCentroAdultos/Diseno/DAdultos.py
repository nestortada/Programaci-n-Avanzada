# Form implementation generated from reading ui file 'C:\Users\nesto\OneDrive - Universidad de la Sabana\AdmonCentroAdultos\Diseno\DAdultos.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdmonAdultos(object):
    def setupUi(self, AdmonAdultos):
        AdmonAdultos.setObjectName("AdmonAdultos")
        AdmonAdultos.resize(1283, 646)
        self.centralwidget = QtWidgets.QWidget(parent=AdmonAdultos)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 1181, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PBTodas = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBTodas.setFont(font)
        self.PBTodas.setObjectName("PBTodas")
        self.gridLayout.addWidget(self.PBTodas, 3, 2, 1, 1)
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
        self.SBCodigoEliminar = QtWidgets.QSpinBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SBCodigoEliminar.setFont(font)
        self.SBCodigoEliminar.setMaximum(999999999)
        self.SBCodigoEliminar.setObjectName("SBCodigoEliminar")
        self.gridLayout.addWidget(self.SBCodigoEliminar, 3, 0, 1, 1)
        self.PBAgregar = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBAgregar.setFont(font)
        self.PBAgregar.setObjectName("PBAgregar")
        self.gridLayout.addWidget(self.PBAgregar, 1, 1, 1, 1)
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
        self.PBSalir = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBSalir.setFont(font)
        self.PBSalir.setObjectName("PBSalir")
        self.gridLayout.addWidget(self.PBSalir, 6, 1, 1, 1)
        self.TWTabla = QtWidgets.QTableWidget(parent=self.layoutWidget)
        self.TWTabla.setMinimumSize(QtCore.QSize(711, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TWTabla.setFont(font)
        self.TWTabla.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.TWTabla.setObjectName("TWTabla")
        self.TWTabla.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.TWTabla.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWTabla.setHorizontalHeaderItem(7, item)
        self.TWTabla.horizontalHeader().setDefaultSectionSize(144)
        self.TWTabla.verticalHeader().setMinimumSectionSize(60)
        self.gridLayout.addWidget(self.TWTabla, 5, 0, 1, 3)
        AdmonAdultos.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=AdmonAdultos)
        self.statusbar.setObjectName("statusbar")
        AdmonAdultos.setStatusBar(self.statusbar)

        self.retranslateUi(AdmonAdultos)
        QtCore.QMetaObject.connectSlotsByName(AdmonAdultos)
        AdmonAdultos.setTabOrder(self.SBCodigoEliminar, self.PBEliminar)
        AdmonAdultos.setTabOrder(self.PBEliminar, self.TWTabla)

    def retranslateUi(self, AdmonAdultos):
        _translate = QtCore.QCoreApplication.translate
        AdmonAdultos.setWindowTitle(_translate("AdmonAdultos", "MainWindow"))
        self.PBTodas.setText(_translate("AdmonAdultos", "Ver Todas"))
        self.PBBuscar.setText(_translate("AdmonAdultos", "Buscar"))
        self.PBEliminar.setText(_translate("AdmonAdultos", "Eliminar"))
        self.PBModificar.setText(_translate("AdmonAdultos", "Modificar"))
        self.LCodigoEliminar.setText(_translate("AdmonAdultos", "Código"))
        self.PBAgregar.setText(_translate("AdmonAdultos", "Agregar"))
        self.LTitulo.setText(_translate("AdmonAdultos", "Administración de Adultos"))
        self.PBSalir.setText(_translate("AdmonAdultos", "Salir"))
        item = self.TWTabla.horizontalHeaderItem(0)
        item.setText(_translate("AdmonAdultos", "Codigo"))
        item = self.TWTabla.horizontalHeaderItem(1)
        item.setText(_translate("AdmonAdultos", "Nombre"))
        item = self.TWTabla.horizontalHeaderItem(2)
        item.setText(_translate("AdmonAdultos", "Apellido"))
        item = self.TWTabla.horizontalHeaderItem(3)
        item.setText(_translate("AdmonAdultos", "Nacimiento"))
        item = self.TWTabla.horizontalHeaderItem(4)
        item.setText(_translate("AdmonAdultos", "Peso"))
        item = self.TWTabla.horizontalHeaderItem(5)
        item.setText(_translate("AdmonAdultos", "Altura"))
        item = self.TWTabla.horizontalHeaderItem(6)
        item.setText(_translate("AdmonAdultos", "Contacto"))
        item = self.TWTabla.horizontalHeaderItem(7)
        item.setText(_translate("AdmonAdultos", "Centro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdmonAdultos = QtWidgets.QMainWindow()
    ui = Ui_AdmonAdultos()
    ui.setupUi(AdmonAdultos)
    AdmonAdultos.show()
    sys.exit(app.exec())
