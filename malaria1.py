from PyQt5 import QtCore, QtGui, QtWidgets
from generating_data_set import Ui_generatingdataset
from dataclassifications import dataclassifications

class Ui_Dialog(object):
    def openWindows(self):
        self.window=QtWidgets.QDialog()
        self.ui = Ui_generatingdataset()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow(self):
        self.window=QtWidgets.QDialog()
        self.ui = dataclassifications()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(979, 491)
        Dialog.setStyleSheet("background-color: rgb(189, 255, 181);\n""background-color: rgb(241, 158, 255);")
        self.okcancel = QtWidgets.QDialogButtonBox(Dialog)
        self.okcancel.setGeometry(QtCore.QRect(340, 290, 171, 32))
        self.okcancel.setOrientation(QtCore.Qt.Horizontal)
        self.okcancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okcancel.setObjectName("okcancel")
        self.malariadetection = QtWidgets.QLabel(Dialog)
        self.malariadetection.setEnabled(True)
        self.malariadetection.setGeometry(QtCore.QRect(70, 20, 771, 37))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.malariadetection.setFont(font)
        self.malariadetection.setObjectName("malariadetection")
        self.chooseoption = QtWidgets.QTextBrowser(Dialog)
        self.chooseoption.setGeometry(QtCore.QRect(120, 130, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.chooseoption.setFont(font)
        self.chooseoption.setObjectName("chooseoption")
        self.Generatingdatasetbutton = QtWidgets.QPushButton(Dialog)
        self.Generatingdatasetbutton.setGeometry(QtCore.QRect(400, 140, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Generatingdatasetbutton.setFont(font)
        self.Generatingdatasetbutton.setObjectName("Generatingdatasetbutton")
        self.Generatingdatasetbutton.clicked.connect(self.openWindows)
        
        self.dataclassificationbutton = QtWidgets.QPushButton(Dialog)
        self.dataclassificationbutton.setGeometry(QtCore.QRect(580, 140, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dataclassificationbutton.setFont(font)
        self.dataclassificationbutton.setObjectName("dataclassificationbutton")
        self.dataclassificationbutton.clicked.connect(self.openWindow)

        self.retranslateUi(Dialog)
        self.okcancel.accepted.connect(Dialog.accept)
        self.okcancel.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Malaria"))
        self.malariadetection.setText(_translate("Dialog", "Malaria Parasites Detection Using Machine Learning"))
        self.chooseoption.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Choose Option:</span></p></body></html>"))
        self.Generatingdatasetbutton.setText(_translate("Dialog", "Genarating data set"))
        self.dataclassificationbutton.setText(_translate("Dialog", "Data Classification"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
