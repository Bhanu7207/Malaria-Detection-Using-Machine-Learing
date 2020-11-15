# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RF_Predictionvalue.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RF_resultsDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(983, 508)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(202, 248, 255);")
        self.okcancel = QtWidgets.QDialogButtonBox(Dialog)
        self.okcancel.setGeometry(QtCore.QRect(370, 430, 171, 32))
        self.okcancel.setOrientation(QtCore.Qt.Horizontal)
        self.okcancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okcancel.setObjectName("okcancel")
        self.RF_Preduiction = QtWidgets.QLabel(Dialog)
        self.RF_Preduiction.setGeometry(QtCore.QRect(150, 30, 671, 51))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(26)
        font.setUnderline(True)
        self.RF_Preduiction.setFont(font)
        self.RF_Preduiction.setObjectName("RF_Preduiction")
        self.predictionvalue = QtWidgets.QLabel(Dialog)
        self.predictionvalue.setGeometry(QtCore.QRect(230, 110, 441, 281))
        self.predictionvalue.setAutoFillBackground(False)
        self.predictionvalue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.predictionvalue.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.predictionvalue.setMidLineWidth(11)
        self.predictionvalue.setText("")
        self.predictionvalue.setPixmap(QtGui.QPixmap("G:/B.tech Project/randomreport.png"))
        self.predictionvalue.setScaledContents(True)
        self.predictionvalue.setWordWrap(False)
        self.predictionvalue.setIndent(1)
        self.predictionvalue.setObjectName("predictionvalue")

        self.retranslateUi(Dialog)
        self.okcancel.accepted.connect(Dialog.accept)
        self.okcancel.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RF_predictionresults"))
        self.RF_Preduiction.setText(_translate("Dialog", "Random Forest Prediction Results"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_RF_resultsDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
