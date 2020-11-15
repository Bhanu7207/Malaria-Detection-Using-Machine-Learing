# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NaiveBayesresultsdialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class NB_results(object):
    def setupUi(self, NaiveBayes):
        NaiveBayes.setObjectName("NaiveBayes")
        NaiveBayes.resize(983, 508)
        NaiveBayes.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        NaiveBayes.setAutoFillBackground(False)
        NaiveBayes.setStyleSheet("background-color: rgb(202, 248, 255);")
        self.okcancel = QtWidgets.QDialogButtonBox(NaiveBayes)
        self.okcancel.setGeometry(QtCore.QRect(370, 430, 171, 32))
        self.okcancel.setOrientation(QtCore.Qt.Horizontal)
        self.okcancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okcancel.setObjectName("okcancel")
        self.Naivebayes = QtWidgets.QLabel(NaiveBayes)
        self.Naivebayes.setGeometry(QtCore.QRect(180, 30, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(26)
        font.setUnderline(True)
        self.Naivebayes.setFont(font)
        self.Naivebayes.setObjectName("Naivebayes")
        self.predictionreport = QtWidgets.QLabel(NaiveBayes)
        self.predictionreport.setGeometry(QtCore.QRect(230, 110, 441, 281))
        self.predictionreport.setAutoFillBackground(False)
        self.predictionreport.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.predictionreport.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.predictionreport.setMidLineWidth(11)
        self.predictionreport.setText("")
        self.predictionreport.setPixmap(QtGui.QPixmap("G:/B.tech Project/Naivereport.png"))
        self.predictionreport.setScaledContents(True)
        self.predictionreport.setWordWrap(False)
        self.predictionreport.setIndent(1)
        self.predictionreport.setObjectName("predictionreport")

        self.retranslateUi(NaiveBayes)
        self.okcancel.accepted.connect(NaiveBayes.accept)
        self.okcancel.rejected.connect(NaiveBayes.reject)
        QtCore.QMetaObject.connectSlotsByName(NaiveBayes)

    def retranslateUi(self, NaiveBayes):
        _translate = QtCore.QCoreApplication.translate
        NaiveBayes.setWindowTitle(_translate("NaiveBayes", "Naive Bayes Results"))
        self.Naivebayes.setText(_translate("NaiveBayes", "Naive Bayes prediction Resuts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NaiveBayes = QtWidgets.QDialog()
    ui = NB_results()
    ui.setupUi(NaiveBayes)
    NaiveBayes.show()
    sys.exit(app.exec_())
