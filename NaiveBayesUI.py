# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NaiveBayesUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from NaiveBayesBackend import NaiveBayesBackend
from NB_results import NB_results
from NB_report import NB_report



class NaiveBayesUI(object):
    def show_popup(self):
        msg= QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Classify Successfully!")
        msg.exec_()
#Naivebayesbackend
    def naivebayesbackend(self):
        self.ui = NaiveBayesBackend()
#Report show button function
    def reportshowbutton(self):
        self.window=QtWidgets.QDialog()
        self.ui = NB_results()
        self.ui.setupUi(self.window)
        self.window.show()
        
#visualizer show button function
    def visualizershowbutton(self):
        self.window=QtWidgets.QDialog()
        self.ui = NB_report()
        self.ui.setupUi(self.window)
        self.window.show()
    
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(869, 586)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Dialog.setStyleSheet("\n""background-color: rgb(3, 255, 24);")
        self.OkCancelButton = QtWidgets.QDialogButtonBox(Dialog)
        self.OkCancelButton.setGeometry(QtCore.QRect(320, 460, 161, 32))
        self.OkCancelButton.setOrientation(QtCore.Qt.Horizontal)
        self.OkCancelButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.OkCancelButton.setObjectName("OkCancelButton")
        self.RandomForestHeading = QtWidgets.QLabel(Dialog)
        self.RandomForestHeading.setGeometry(QtCore.QRect(100, 10, 651, 101))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.RandomForestHeading.setFont(font)
        self.RandomForestHeading.setObjectName("RandomForestHeading")
        self.ChooseYourActivity = QtWidgets.QLabel(Dialog)
        self.ChooseYourActivity.setGeometry(QtCore.QRect(130, 120, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.ChooseYourActivity.setFont(font)
        self.ChooseYourActivity.setObjectName("ChooseYourActivity")
        
#classifybutton
        self.ClassifyButton = QtWidgets.QPushButton(Dialog)
        self.ClassifyButton.setGeometry(QtCore.QRect(410, 140, 171, 41))
        self.ClassifyButton.setObjectName("ClassifyButton")
        self.ClassifyButton.clicked.connect(self.show_popup)
        self.ClassifyButton.clicked.connect(self.naivebayesbackend)
        
#reportbutton
        self.ReportButton = QtWidgets.QPushButton(Dialog)
        self.ReportButton.setGeometry(QtCore.QRect(410, 290, 161, 31))
        self.ReportButton.setObjectName("ReportButton")
        self.ReportButton.clicked.connect(self.reportshowbutton)
        self.CheckResultsActivityy = QtWidgets.QLabel(Dialog)
        self.CheckResultsActivityy.setGeometry(QtCore.QRect(120, 220, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.CheckResultsActivityy.setFont(font)
        self.CheckResultsActivityy.setObjectName("CheckResultsActivityy")
#predicitionreport
        self.PredictionReport = QtWidgets.QLabel(Dialog)
        self.PredictionReport.setGeometry(QtCore.QRect(230, 290, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PredictionReport.setFont(font)
        self.PredictionReport.setObjectName("PredictionReport")
#visualisingdatabutton
        self.VisualisingDataReport = QtWidgets.QLabel(Dialog)
        self.VisualisingDataReport.setGeometry(QtCore.QRect(170, 360, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.VisualisingDataReport.setFont(font)
        self.VisualisingDataReport.setObjectName("VisualisingDataReport")
        self.Visualizer = QtWidgets.QPushButton(Dialog)
        self.Visualizer.setGeometry(QtCore.QRect(400, 360, 161, 31))
        self.Visualizer.setObjectName("Visualizer")
        self.Visualizer.clicked.connect(self.visualizershowbutton)

        self.retranslateUi(Dialog)
        self.OkCancelButton.accepted.connect(Dialog.accept)
        self.OkCancelButton.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NaiveBayesUI"))
        self.RandomForestHeading.setText(_translate("Dialog", "Naive Bayes Classification"))
        self.ChooseYourActivity.setText(_translate("Dialog", "Choose Your Activity:"))
        self.ClassifyButton.setText(_translate("Dialog", "Classify the Inputs"))
        self.ReportButton.setText(_translate("Dialog", "Report"))
        self.CheckResultsActivityy.setText(_translate("Dialog", "Check Results Activity:"))
        self.PredictionReport.setText(_translate("Dialog", "Prediction Report:"))
        self.VisualisingDataReport.setText(_translate("Dialog", "Visualising Data Report: "))
        self.Visualizer.setText(_translate("Dialog", "Visualizer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = NaiveBayesUI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
