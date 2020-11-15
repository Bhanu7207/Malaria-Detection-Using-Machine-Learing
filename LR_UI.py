# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogisticRegressionUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from LR_backend import LR_backend
from LR_results import LR_results
from LR_report import LR_report



class LR_UI(object):
    def show_popup(self):
        msg= QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Classify Successfully!")
        msg.exec_()
#LR_backend
    def LR_backend(self):
        self.ui = LR_backend()
#Report show button function
    def reportshowbutton(self):
        self.window=QtWidgets.QDialog()
        self.ui = LR_results()
        self.ui.setupUi(self.window)
        self.window.show()
        
#visualizer show button function
    def visualizershowbutton(self):
        self.window=QtWidgets.QDialog()
        self.ui = LR_report()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(996, 568)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(360, 510, 171, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.headinglogistic = QtWidgets.QLabel(Dialog)
        self.headinglogistic.setGeometry(QtCore.QRect(90, 30, 831, 101))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.headinglogistic.setFont(font)
        self.headinglogistic.setObjectName("headinglogistic")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 140, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
#Classifybutton
        self.ClassifypushButton = QtWidgets.QPushButton(Dialog)
        self.ClassifypushButton.setGeometry(QtCore.QRect(460, 170, 181, 31))
        self.ClassifypushButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.ClassifypushButton.setObjectName("ClassifypushButton")
        self.ClassifypushButton.clicked.connect(self.show_popup)
        self.ClassifypushButton.clicked.connect(self.LR_backend)
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 230, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 300, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
#reportbutton
        self.ReportpushButton_2 = QtWidgets.QPushButton(Dialog)
        self.ReportpushButton_2.setGeometry(QtCore.QRect(460, 330, 181, 31))
        self.ReportpushButton_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.ReportpushButton_2.setObjectName("ReportpushButton_2")
        self.ReportpushButton_2.clicked.connect(self.reportshowbutton)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(250, 390, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
#Visualizerbutton
        self.VisualizerpushButton_3 = QtWidgets.QPushButton(Dialog)
        self.VisualizerpushButton_3.setGeometry(QtCore.QRect(460, 420, 181, 31))
        self.VisualizerpushButton_3.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.VisualizerpushButton_3.setObjectName("VisualizerpushButton_3")
        self.VisualizerpushButton_3.clicked.connect(self.visualizershowbutton)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Logistic Regression Classification"))
        self.headinglogistic.setText(_translate("Dialog", "Logistic Regression Classification "))
        self.label.setText(_translate("Dialog", "Choose Your Activity:"))
        self.ClassifypushButton.setText(_translate("Dialog", "Classify the Inputs"))
        self.label_2.setText(_translate("Dialog", "Check Results Activity:"))
        self.label_3.setText(_translate("Dialog", "Prediction Report:"))
        self.ReportpushButton_2.setText(_translate("Dialog", "Report"))
        self.label_4.setText(_translate("Dialog", "Visualising Data Report:"))
        self.VisualizerpushButton_3.setText(_translate("Dialog", "Visualizer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LR_UI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
