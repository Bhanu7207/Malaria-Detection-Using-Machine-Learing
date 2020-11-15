# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NaiveBayesreportdialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class NB_report(object):
    def setupUi(self, naivebayes):
        naivebayes.setObjectName("naivebayes")
        naivebayes.resize(983, 508)
        naivebayes.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        naivebayes.setAutoFillBackground(False)
        naivebayes.setStyleSheet("background-color: rgb(202, 248, 255);")
        self.okcancel = QtWidgets.QDialogButtonBox(naivebayes)
        self.okcancel.setGeometry(QtCore.QRect(370, 430, 171, 32))
        self.okcancel.setOrientation(QtCore.Qt.Horizontal)
        self.okcancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okcancel.setObjectName("okcancel")
        self.Naivebayes_report = QtWidgets.QLabel(naivebayes)
        self.Naivebayes_report.setGeometry(QtCore.QRect(280, 30, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(26)
        font.setUnderline(True)
        self.Naivebayes_report.setFont(font)
        self.Naivebayes_report.setObjectName("Naivebayes_report")
        self.predictionreport = QtWidgets.QLabel(naivebayes)
        self.predictionreport.setGeometry(QtCore.QRect(230, 110, 441, 281))
        self.predictionreport.setAutoFillBackground(False)
        self.predictionreport.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.predictionreport.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.predictionreport.setMidLineWidth(11)
        self.predictionreport.setText("")
        self.predictionreport.setPixmap(QtGui.QPixmap("G:/B.tech Project/Naiveresult.png"))
        self.predictionreport.setScaledContents(True)
        self.predictionreport.setWordWrap(False)
        self.predictionreport.setIndent(1)
        self.predictionreport.setObjectName("predictionreport")

        self.retranslateUi(naivebayes)
        self.okcancel.accepted.connect(naivebayes.accept)
        self.okcancel.rejected.connect(naivebayes.reject)
        QtCore.QMetaObject.connectSlotsByName(naivebayes)

    def retranslateUi(self, naivebayes):
        _translate = QtCore.QCoreApplication.translate
        naivebayes.setWindowTitle(_translate("naivebayes", "Naive Bayes report"))
        self.Naivebayes_report.setText(_translate("naivebayes", "Naive Bayes Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    naivebayes = QtWidgets.QDialog()
    ui = NB_report()
    ui.setupUi(naivebayes)
    naivebayes.show()
    sys.exit(app.exec_())
