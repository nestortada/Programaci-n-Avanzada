# Form implementation generated from reading ui file 'C:\Users\nesto\OneDrive - Universidad de la Sabana\Diseño proyecto final\Diseno\DModificarInscripcion.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ModificarInscripcion(object):
    def setupUi(self, ModificarInscripcion):
        ModificarInscripcion.setObjectName("ModificarInscripcion")
        ModificarInscripcion.resize(552, 490)
        self.centralwidget = QtWidgets.QWidget(parent=ModificarInscripcion)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 80, 431, 186))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PBAgregar = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.PBAgregar.setObjectName("PBAgregar")
        self.gridLayout.addWidget(self.PBAgregar, 7, 1, 1, 1)
        self.CodigoACtividad = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.CodigoACtividad.setMaximum(999999999)
        self.CodigoACtividad.setObjectName("CodigoACtividad")
        self.gridLayout.addWidget(self.CodigoACtividad, 3, 1, 1, 1)
        self.PBSalir = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.PBSalir.setObjectName("PBSalir")
        self.gridLayout.addWidget(self.PBSalir, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.CodigoAdulto = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.CodigoAdulto.setMaximum(999999999)
        self.CodigoAdulto.setObjectName("CodigoAdulto")
        self.gridLayout.addWidget(self.CodigoAdulto, 2, 1, 1, 1)
        self.CBCali = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.CBCali.setObjectName("CBCali")
        self.gridLayout.addWidget(self.CBCali, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.Calificacion = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.Calificacion.setMaximum(10)
        self.Calificacion.setObjectName("Calificacion")
        self.gridLayout.addWidget(self.Calificacion, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
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
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.CodigoAdultoViejo = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.CodigoAdultoViejo.setMaximum(999999999)
        self.CodigoAdultoViejo.setObjectName("CodigoAdultoViejo")
        self.gridLayout.addWidget(self.CodigoAdultoViejo, 5, 1, 1, 1)
        self.CodigoACtividadVieja = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.CodigoACtividadVieja.setMaximum(999999999)
        self.CodigoACtividadVieja.setObjectName("CodigoACtividadVieja")
        self.gridLayout.addWidget(self.CodigoACtividadVieja, 6, 1, 1, 1)
        ModificarInscripcion.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=ModificarInscripcion)
        self.statusbar.setObjectName("statusbar")
        ModificarInscripcion.setStatusBar(self.statusbar)

        self.retranslateUi(ModificarInscripcion)
        QtCore.QMetaObject.connectSlotsByName(ModificarInscripcion)

    def retranslateUi(self, ModificarInscripcion):
        _translate = QtCore.QCoreApplication.translate
        ModificarInscripcion.setWindowTitle(_translate("ModificarInscripcion", "MainWindow"))
        self.PBAgregar.setText(_translate("ModificarInscripcion", "Modificar"))
        self.PBSalir.setText(_translate("ModificarInscripcion", "Salir"))
        self.label_5.setText(_translate("ModificarInscripcion", "Adulto Viejo"))
        self.CBCali.setText(_translate("ModificarInscripcion", "No hay calificacion"))
        self.label_4.setText(_translate("ModificarInscripcion", "Calificacion"))
        self.label_3.setText(_translate("ModificarInscripcion", "Codigo Actividad"))
        self.label_2.setText(_translate("ModificarInscripcion", "Codigo Adulto"))
        self.LTitulo.setText(_translate("ModificarInscripcion", "Modificar Inscripcion"))
        self.label_6.setText(_translate("ModificarInscripcion", "Actividad Vieja"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModificarInscripcion = QtWidgets.QMainWindow()
    ui = Ui_ModificarInscripcion()
    ui.setupUi(ModificarInscripcion)
    ModificarInscripcion.show()
    sys.exit(app.exec())
