# Form implementation generated from reading ui file 'C:\Users\nesto\OneDrive - Universidad de la Sabana\AdmonCentroAdultos\Diseno\DConsultas.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdmonConsultas(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 420)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BTerminar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BTerminar.setGeometry(QtCore.QRect(260, 350, 619, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BTerminar.setFont(font)
        self.BTerminar.setObjectName("BTerminar")
        self.LTitulo = QtWidgets.QLabel(parent=self.centralwidget)
        self.LTitulo.setGeometry(QtCore.QRect(110, 30, 617, 33))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(18)
        self.LTitulo.setFont(font)
        self.LTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LTitulo.setObjectName("LTitulo")
        self.BLAM = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BLAM.setGeometry(QtCore.QRect(10, 90, 401, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BLAM.setFont(font)
        self.BLAM.setObjectName("BLAM")
        self.BEx = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BEx.setGeometry(QtCore.QRect(600, 80, 341, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BEx.setFont(font)
        self.BEx.setObjectName("BEx")
        self.BLAF = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BLAF.setGeometry(QtCore.QRect(20, 230, 341, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BLAF.setFont(font)
        self.BLAF.setObjectName("BLAF")
        self.BLIA = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BLIA.setGeometry(QtCore.QRect(610, 220, 341, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BLIA.setFont(font)
        self.BLIA.setObjectName("BLIA")
        self.BCAA = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BCAA.setGeometry(QtCore.QRect(310, 150, 341, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BCAA.setFont(font)
        self.BCAA.setObjectName("BCAA")
        self.BAC = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BAC.setGeometry(QtCore.QRect(320, 290, 341, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BAC.setFont(font)
        self.BAC.setObjectName("BAC")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyectos de Facultad"))
        self.BTerminar.setText(_translate("MainWindow", "Terminar"))
        self.LTitulo.setText(_translate("MainWindow", "Consultas"))
        self.BLAM.setText(_translate("MainWindow", "Listado de Adultos Mayores por Centro"))
        self.BEx.setText(_translate("MainWindow", "Extra: Actividades por centro"))
        self.BLAF.setText(_translate("MainWindow", "Listado de Actividades Futuras"))
        self.BLIA.setText(_translate("MainWindow", "Listado de Inscritos en Actividades"))
        self.BCAA.setText(_translate("MainWindow", "Calificacion de una Actividad"))
        self.BAC.setText(_translate("MainWindow", "Actividades Realizadas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AdmonConsultas()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
