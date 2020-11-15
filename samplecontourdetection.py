# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'samplecontourdetection.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class samplecontourdetection(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(772, 399)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(202, 248, 255);")
        self.okcancel = QtWidgets.QDialogButtonBox(Dialog)
        self.okcancel.setGeometry(QtCore.QRect(290, 330, 171, 32))
        self.okcancel.setOrientation(QtCore.Qt.Horizontal)
        self.okcancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okcancel.setObjectName("okcancel")
        self.samplecontour = QtWidgets.QLabel(Dialog)
        self.samplecontour.setGeometry(QtCore.QRect(60, 20, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(26)
        font.setUnderline(True)
        self.samplecontour.setFont(font)
        self.samplecontour.setObjectName("samplecontour")
        self.image = QtWidgets.QLabel(Dialog)
        self.image.setGeometry(QtCore.QRect(260, 110, 241, 181))
        self.image.setAutoFillBackground(False)
        self.image.setFrameShape(QtWidgets.QFrame.Box)
        self.image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.image.setMidLineWidth(11)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("2.png"))
        self.image.setScaledContents(True)
        self.image.setWordWrap(False)
        self.image.setIndent(1)
        self.image.setObjectName("image")

        self.retranslateUi(Dialog)
        self.okcancel.accepted.connect(Dialog.accept)
        self.okcancel.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "samplecontourdetection"))
        self.samplecontour.setText(_translate("Dialog", "Sample Contour Detetction Iimage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = samplecontourdetection()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
