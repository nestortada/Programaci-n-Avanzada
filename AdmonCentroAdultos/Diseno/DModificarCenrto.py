# Form implementation generated from reading ui file 'C:\Users\nesto\OneDrive - Universidad de la Sabana\Diseño proyecto final\Diseno\DModificarCentro.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ModificarCentros(object):
    def setupUi(self, ModificarCentros):
        ModificarCentros.setObjectName("ModificarCentros")
        ModificarCentros.resize(552, 490)
        self.centralwidget = QtWidgets.QWidget(parent=ModificarCentros)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 130, 431, 160))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Nombre = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.Nombre.setMaxLength(30)
        self.Nombre.setObjectName("Nombre")
        self.gridLayout.addWidget(self.Nombre, 2, 1, 1, 1)
        self.PBSalir = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.PBSalir.setObjectName("PBSalir")
        self.gridLayout.addWidget(self.PBSalir, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
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
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.Direccion = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.Direccion.setMaxLength(45)
        self.Direccion.setObjectName("Direccion")
        self.gridLayout.addWidget(self.Direccion, 3, 1, 1, 1)
        self.Telefono = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.Telefono.setMaxLength(45)
        self.Telefono.setObjectName("Telefono")
        self.gridLayout.addWidget(self.Telefono, 4, 1, 1, 1)
        self.PBAgregar = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.PBAgregar.setObjectName("PBAgregar")
        self.gridLayout.addWidget(self.PBAgregar, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.NombreViejo = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.NombreViejo.setMaxLength(30)
        self.NombreViejo.setObjectName("NombreViejo")
        self.gridLayout.addWidget(self.NombreViejo, 5, 1, 1, 1)
        ModificarCentros.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=ModificarCentros)
        self.statusbar.setObjectName("statusbar")
        ModificarCentros.setStatusBar(self.statusbar)

        self.retranslateUi(ModificarCentros)
        QtCore.QMetaObject.connectSlotsByName(ModificarCentros)

    def retranslateUi(self, ModificarCentros):
        _translate = QtCore.QCoreApplication.translate
        ModificarCentros.setWindowTitle(_translate("ModificarCentros", "MainWindow"))
        self.PBSalir.setText(_translate("ModificarCentros", "Salir"))
        self.label_2.setText(_translate("ModificarCentros", "Nombre"))
        self.LTitulo.setText(_translate("ModificarCentros", "Modificar Centros"))
        self.label_4.setText(_translate("ModificarCentros", "Telefono"))
        self.PBAgregar.setText(_translate("ModificarCentros", "Modificar"))
        self.label_3.setText(_translate("ModificarCentros", "Direccion"))
        self.label_5.setText(_translate("ModificarCentros", "Nombre Viejo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModificarCentros = QtWidgets.QMainWindow()
    ui = Ui_ModificarCentros()
    ui.setupUi(ModificarCentros)
    ModificarCentros.show()
    sys.exit(app.exec())