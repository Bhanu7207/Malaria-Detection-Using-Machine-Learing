# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logisticreportdialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class LR_report(object):
    def setupUi(self, logistic):
        logistic.setObjectName("logistic")
        logistic.resize(983, 508)
        logistic.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        logistic.setAutoFillBackground(False)
        logistic.setStyleSheet("background-color: rgb(202, 248, 255);")
        self.okcancel = QtWidgets.QDialogButtonBox(logistic)
        self.okcancel.setGeometry(QtCore.QRect(370, 430, 171, 32))
        self.okcancel.setOrientation(QtCore.Qt.Horizontal)
        self.okcancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okcancel.setObjectName("okcancel")
        self.logistic_report = QtWidgets.QLabel(logistic)
        self.logistic_report.setGeometry(QtCore.QRect(180, 30, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(26)
        font.setUnderline(True)
        self.logistic_report.setFont(font)
        self.logistic_report.setObjectName("logistic_report")
        self.predictionreport = QtWidgets.QLabel(logistic)
        self.predictionreport.setGeometry(QtCore.QRect(230, 110, 441, 281))
        self.predictionreport.setAutoFillBackground(False)
        self.predictionreport.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.predictionreport.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.predictionreport.setMidLineWidth(11)
        self.predictionreport.setText("")
        self.predictionreport.setPixmap(QtGui.QPixmap("G:/B.tech Project/logisticreport.png"))
        self.predictionreport.setScaledContents(True)
        self.predictionreport.setWordWrap(False)
        self.predictionreport.setIndent(1)
        self.predictionreport.setObjectName("predictionreport")

        self.retranslateUi(logistic)
        self.okcancel.accepted.connect(logistic.accept)
        self.okcancel.rejected.connect(logistic.reject)
        QtCore.QMetaObject.connectSlotsByName(logistic)

    def retranslateUi(self, logistic):
        _translate = QtCore.QCoreApplication.translate
        logistic.setWindowTitle(_translate("logistic", "logisticreport"))
        self.logistic_report.setText(_translate("logistic", "Logistic Regression Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    logistic = QtWidgets.QDialog()
    ui = LR_report()
    ui.setupUi(logistic)
    logistic.show()
    sys.exit(app.exec_())
