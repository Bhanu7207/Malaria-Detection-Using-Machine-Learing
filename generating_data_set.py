# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generating_data_set.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QFileDialog,QMessageBox,QToolButton
from samplecontourdetection import samplecontourdetection
from PyQt5.QtGui import *
from preprocessordialog import Ui_preprocessordialog

class Ui_generatingdataset(object):
    def openWindows(self):
        self.window=QtWidgets.QDialog()
        self.ui = Ui_preprocessordialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindows1(self):
        self.window=QtWidgets.QDialog()
        self.ui = samplecontourdetection()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def home(self):
        btn = QtWidgets.QPushButton("upload", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)
    
    def download(self):
       self.completed=0
       while self.completed < 100:
           self.completed += 0.0001
           self.loadingbar.setValue(self.completed)

    
    def pushButton_handler(self):
        print("Button pressed")
        self.open_dialog_box()
        
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)
        with open(path, "r") as f:
            print("upload successfully")
            print(f.readline())
    
    def show_popup1(self):
        msg1=QMessageBox()
        msg1.setWindowTitle("Preview")
        msg1.setText("Show the Picture")
        msg1.setIcon(QMessageBox.Question)
        msg1.setStandardButtons(QMessageBox.Ok)
        msg1.setDefaultButton(QMessageBox.Retry)
        msg1.setLayout("1.jpg")
    def show_popup(self):
        msg= QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Please classify the data first!")
        msg.exec_()

        
    def setupUi(self, generatingdataset):
        generatingdataset.setObjectName("generatingdataset")
        generatingdataset.setEnabled(True)
        generatingdataset.resize(809, 522)
        generatingdataset.setStyleSheet("background-color: rgb(151, 151, 255);")
        self.generatingdatasetlabel = QtWidgets.QLabel(generatingdataset)
        self.generatingdatasetlabel.setGeometry(QtCore.QRect(80, 20, 681, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.generatingdatasetlabel.setFont(font)
        self.generatingdatasetlabel.setStyleSheet("")
        self.generatingdatasetlabel.setObjectName("generatingdatasetlabel")
        self.widgettab1 = QtWidgets.QTabWidget(generatingdataset)
        self.widgettab1.setGeometry(QtCore.QRect(70, 90, 681, 291))
        self.widgettab1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.widgettab1.setObjectName("widgettab1")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        
    #openbutton
        self.openbutton = QtWidgets.QPushButton(self.tab1)
        self.openbutton.setGeometry(QtCore.QRect(420, 70, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.openbutton.setFont(font)
        self.openbutton.setStyleSheet("border-top-color: rgb(255, 58, 58);")
        self.openbutton.setObjectName("openbutton")
        self.openbutton.clicked.connect(self.pushButton_handler)
    #label   
        self.label_2 = QtWidgets.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
    #loadingbar
        self.loadingbar = QtWidgets.QProgressBar(self.tab1)
        self.loadingbar.setGeometry(QtCore.QRect(190, 150, 321, 20))
        self.loadingbar.setObjectName("loadingbar")
    #btn button
        self.btn = QtWidgets.QPushButton(self.tab1)
        self.btn.setGeometry(QtCore.QRect(310, 200, 75, 23))
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.download)
        self.widgettab1.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        
        
    #preprocessorssbutton
        self.preprocessorsbutton = QtWidgets.QToolButton(self.tab_2)
        self.preprocessorsbutton.setGeometry(QtCore.QRect(40, 170, 261, 41))
        self.preprocessorsbutton.setStyleSheet("ewfefewf")
        self.preprocessorsbutton.setObjectName("preprocessorsbutton")
        self.preprocessorsbutton.clicked.connect(self.openWindows)
        self.sampleactivitylabel = QtWidgets.QLabel(self.tab_2)
        self.sampleactivitylabel.setGeometry(QtCore.QRect(150, 50, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
    #sampleactivity
        self.sampleactivitylabel.setFont(font)
        self.sampleactivitylabel.setObjectName("sampleactivitylabel")
    #contourdetection button
        self.contourdetectionbutton = QtWidgets.QToolButton(self.tab_2)
        self.contourdetectionbutton.setGeometry(QtCore.QRect(390, 170, 271, 41))
        self.contourdetectionbutton.setObjectName("contourdetectionbutton")
        self.contourdetectionbutton.clicked.connect(self.openWindows1)
        self.widgettab1.addTab(self.tab_2, "")
    #okcancel button
        self.okcancelbutton = QtWidgets.QDialogButtonBox(generatingdataset)
        self.okcancelbutton.setGeometry(QtCore.QRect(360, 400, 161, 51))
        self.okcancelbutton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okcancelbutton.setObjectName("okcancelbutton")
        self.okcancelbutton.clicked.connect(self.show_popup)

        self.retranslateUi(generatingdataset)
        self.widgettab1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(generatingdataset)
    

    def retranslateUi(self, generatingdataset):
        _translate = QtCore.QCoreApplication.translate
        generatingdataset.setWindowTitle(_translate("generatingdataset", "generating dataset"))
        self.generatingdatasetlabel.setText(_translate("generatingdataset", "Generating Data Set Of Given Samples"))
        self.openbutton.setText(_translate("generatingdataset", "Open"))
        self.label_2.setText(_translate("generatingdataset", "Upload Your Samples:"))
        self.btn.setText(_translate("generatingdataset", "Upload"))
        self.widgettab1.setTabText(self.widgettab1.indexOf(self.tab1), _translate("generatingdataset", "UploadTab"))
        self.preprocessorsbutton.setText(_translate("generatingdataset", "Preview Processors Image Samples"))
        self.sampleactivitylabel.setText(_translate("generatingdataset", "Choose the Sample Activity"))
        self.contourdetectionbutton.setText(_translate("generatingdataset", "Contour Detection Image Samples "))
        self.widgettab1.setTabText(self.widgettab1.indexOf(self.tab_2), _translate("generatingdataset", "ActivityTab"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    generatingdataset = QtWidgets.QDialog()
    ui = Ui_generatingdataset()
    ui.setupUi(generatingdataset)
    generatingdataset.show()
    sys.exit(app.exec_())
