# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(338, 185)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(252, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_fDate = QtWidgets.QTextEdit(Dialog)
        self.textEdit_fDate.setGeometry(QtCore.QRect(112, 86, 151, 31))
        self.textEdit_fDate.setObjectName("textEdit_fDate")
        self.textEdit_MMSI = QtWidgets.QTextEdit(Dialog)
        self.textEdit_MMSI.setGeometry(QtCore.QRect(112, 33, 151, 31))
        self.textEdit_MMSI.setObjectName("textEdit_MMSI")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(52, 94, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 61, 16))
        self.label_2.setObjectName("label_2")
        self.Cancel = QtWidgets.QPushButton(Dialog)
        self.Cancel.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.Cancel.setObjectName("Cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.label.setText(_translate("Dialog", "Date"))
        self.label_2.setText(_translate("Dialog", "MMSI"))
        self.Cancel.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

