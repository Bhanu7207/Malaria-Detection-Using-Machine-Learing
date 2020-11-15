# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RandomForestUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from random_forest_tarak import ui_random_forest_tarak
from Ui_RF_resultsDialog import Ui_RF_resultsDialog
from RF_Report import RF_Report


class RandomForestUI(object):
    
    def show_popup(self):
        msg= QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Classify Successfully!")
        msg.exec_()
    
    def randomforestbackend(self):
        #self.window=QtWidgets.QDialog()
        self.ui = ui_random_forest_tarak()
        #self.ui.setupUi(self.window)
        #self.window.show()
        
#Report show button function
    def reportshowbutton(self):
        self.window=QtWidgets.QDialog()
        self.ui = Ui_RF_resultsDialog()
        self.ui.setupUi(self.window)
        self.window.show()
        
#visualizer show button function
    def visualizershowbutton(self):
        self.window=QtWidgets.QDialog()
        self.ui = RF_Report()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(869, 586)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Dialog.setStyleSheet("\n""background-color: rgb(255, 120, 140);")
        self.OkCancelButton = QtWidgets.QDialogButtonBox(Dialog)
        self.OkCancelButton.setGeometry(QtCore.QRect(380, 520, 161, 32))
        self.OkCancelButton.setOrientation(QtCore.Qt.Horizontal)
        self.OkCancelButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.OkCancelButton.setObjectName("OkCancelButton")
        self.RandomForestHeading = QtWidgets.QLabel(Dialog)
        self.RandomForestHeading.setGeometry(QtCore.QRect(90, 20, 711, 71))
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
#Classifty button
        self.ClassifyButton = QtWidgets.QPushButton(Dialog)
        self.ClassifyButton.setGeometry(QtCore.QRect(410, 140, 171, 41))
        self.ClassifyButton.setObjectName("ClassifyButton")
        self.ClassifyButton.clicked.connect(self.show_popup)
        self.ClassifyButton.clicked.connect(self.randomforestbackend)
        
#Report BUtton
        self.ReportButton = QtWidgets.QPushButton(Dialog)
        self.ReportButton.setGeometry(QtCore.QRect(420, 370, 161, 31))
        self.ReportButton.setObjectName("ReportButton")
        self.ReportButton.clicked.connect(self.reportshowbutton)
        self.CheckResultsActivityy = QtWidgets.QLabel(Dialog)
        self.CheckResultsActivityy.setGeometry(QtCore.QRect(130, 300, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.CheckResultsActivityy.setFont(font)
        self.CheckResultsActivityy.setObjectName("CheckResultsActivityy")
        
#predictionReport
        self.PredictionReport = QtWidgets.QLabel(Dialog)
        self.PredictionReport.setGeometry(QtCore.QRect(240, 370, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PredictionReport.setFont(font)
        self.PredictionReport.setObjectName("PredictionReport")
        
        
        self.VisualisingDataReport = QtWidgets.QLabel(Dialog)
        self.VisualisingDataReport.setGeometry(QtCore.QRect(180, 440, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.VisualisingDataReport.setFont(font)
        self.VisualisingDataReport.setObjectName("VisualisingDataReport")
        
#Visualizer button
        self.Visualizer = QtWidgets.QPushButton(Dialog)
        self.Visualizer.setGeometry(QtCore.QRect(410, 440, 161, 31))
        self.Visualizer.setObjectName("Visualizer")
        self.Visualizer.clicked.connect(self.visualizershowbutton)

        self.retranslateUi(Dialog)
        self.OkCancelButton.accepted.connect(Dialog.accept)
        self.OkCancelButton.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RandomForestUI"))
        self.RandomForestHeading.setText(_translate("Dialog", "Random Forest Classification "))
        self.ChooseYourActivity.setText(_translate("Dialog", "Choose Your Activity:"))
        self.ClassifyButton.setText(_translate("Dialog", "Classify the Inputs"))
     #  self.ProcessingStatus.setText(_translate("Dialog", "Processing status:"))
        self.ReportButton.setText(_translate("Dialog", "Report"))
        self.CheckResultsActivityy.setText(_translate("Dialog", "Check Results Activity:"))
        self.PredictionReport.setText(_translate("Dialog", "Prediction Report:"))
        self.VisualisingDataReport.setText(_translate("Dialog", "Visualising Data Report: "))
        self.Visualizer.setText(_translate("Dialog", "Visualizer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = RandomForestUI()
    #ui= Ui_RF_resultsDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
