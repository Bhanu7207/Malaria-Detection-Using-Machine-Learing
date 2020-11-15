# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataclassification.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from RandomForestUI import RandomForestUI
from NaiveBayesUI import NaiveBayesUI
from LR_UI import LR_UI
#import sys
#sys.path.append('C:/Users/rocks/OneDrive/Documents/QT designer/RandomForest/RandomForestUI')
#sys.path.append("/path/to/my/modules/")
#import  RandomForestUI




class dataclassifications(object):
#randomforestbuttonshow
    def Randomforestbuttonshow(self):
        self.window=QtWidgets.QDialog()
        self.ui = RandomForestUI()
        self.ui.setupUi(self.window)
        self.window.show()
#Naivebayesbuttonshow
    def NaiveBayesUIshow(self):
        self.window=QtWidgets.QDialog()
        self.ui = NaiveBayesUI()
        self.ui.setupUi(self.window)
        self.window.show()
#Logisticregressionbuttonshow
    def LR_UIshow(self):
        self.window=QtWidgets.QDialog()
        self.ui = LR_UI()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, dataclassification):
        dataclassification.setObjectName("dataclassification")
        dataclassification.resize(851, 556)
        dataclassification.setStyleSheet("\n""background-color: rgb(142, 142, 255);")
        self.okcancelbutton = QtWidgets.QDialogButtonBox(dataclassification)
        self.okcancelbutton.setGeometry(QtCore.QRect(300, 420, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.okcancelbutton.setFont(font)
        self.okcancelbutton.setOrientation(QtCore.Qt.Horizontal)
        self.okcancelbutton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okcancelbutton.setObjectName("okcancelbutton")
        self.dataclassificationlabel = QtWidgets.QLabel(dataclassification)
        self.dataclassificationlabel.setGeometry(QtCore.QRect(280, 20, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.dataclassificationlabel.setFont(font)
        self.dataclassificationlabel.setObjectName("dataclassificationlabel")
        self.chooseclassificationmethodlabel = QtWidgets.QLabel(dataclassification)
        self.chooseclassificationmethodlabel.setGeometry(QtCore.QRect(30, 110, 481, 121))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.chooseclassificationmethodlabel.setFont(font)
        self.chooseclassificationmethodlabel.setObjectName("chooseclassificationmethodlabel")
#Random Forest Button
        
        self.randomforestbutton = QtWidgets.QToolButton(dataclassification)
        self.randomforestbutton.setGeometry(QtCore.QRect(530, 160, 121, 31))
        self.randomforestbutton.setObjectName("randomforestbutton")
        self.randomforestbutton.clicked.connect(self.Randomforestbuttonshow)
#Naive bayes button
        
        self.naivebayesbutton = QtWidgets.QToolButton(dataclassification)
        self.naivebayesbutton.setGeometry(QtCore.QRect(530, 230, 121, 31))
        self.naivebayesbutton.setObjectName("naivebayesbutton")
        self.naivebayesbutton.clicked.connect(self.NaiveBayesUIshow)
#Logistic Regression Button
        
        self.logisticregressionbutton = QtWidgets.QToolButton(dataclassification)
        self.logisticregressionbutton.setGeometry(QtCore.QRect(530, 300, 121, 31))
        self.logisticregressionbutton.setObjectName("logisticregressionbutton")
        self.logisticregressionbutton.clicked.connect(self.LR_UIshow)


        self.retranslateUi(dataclassification)
        self.okcancelbutton.accepted.connect(dataclassification.accept)
        self.okcancelbutton.rejected.connect(dataclassification.reject)
        QtCore.QMetaObject.connectSlotsByName(dataclassification)

    def retranslateUi(self, dataclassification):
        _translate = QtCore.QCoreApplication.translate
        dataclassification.setWindowTitle(_translate("dataclassification", "Dialog"))
        self.dataclassificationlabel.setText(_translate("dataclassification", "Data Classification"))
        self.chooseclassificationmethodlabel.setText(_translate("dataclassification", "Choose Classification Method:"))
        self.randomforestbutton.setText(_translate("dataclassification", "Random Forest"))
        self.naivebayesbutton.setText(_translate("dataclassification", "Naive bayes"))
        self.logisticregressionbutton.setText(_translate("dataclassification", "Logistic Regression"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dataclassification = QtWidgets.QDialog()
    ui = dataclassifications()
    ui.setupUi(dataclassification)
    dataclassification.show()
    sys.exit(app.exec_())
