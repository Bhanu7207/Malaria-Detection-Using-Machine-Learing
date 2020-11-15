# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RF_Report.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class RF_Report(object):
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
        self.RF_Report = QtWidgets.QLabel(Dialog)
        self.RF_Report.setGeometry(QtCore.QRect(240, 30, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(26)
        font.setUnderline(True)
        self.RF_Report.setFont(font)
        self.RF_Report.setObjectName("RF_Report")
        self.randomreport = QtWidgets.QLabel(Dialog)
        self.randomreport.setGeometry(QtCore.QRect(230, 110, 441, 281))
        self.randomreport.setAutoFillBackground(False)
        self.randomreport.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.randomreport.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.randomreport.setMidLineWidth(11)
        self.randomreport.setText("")
        self.randomreport.setPixmap(QtGui.QPixmap("G:/B.tech Project/randomforest.png"))
        self.randomreport.setScaledContents(True)
        self.randomreport.setWordWrap(False)
        self.randomreport.setIndent(1)
        self.randomreport.setObjectName("randomreport")

        self.retranslateUi(Dialog)
        self.okcancel.accepted.connect(Dialog.accept)
        self.okcancel.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RF_Report "))
        self.RF_Report.setText(_translate("Dialog", "Random Forest Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = RF_Report()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
