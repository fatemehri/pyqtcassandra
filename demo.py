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
        Dialog.resize(342, 245)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(252, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(57, 74, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 27, 61, 16))
        self.label_2.setObjectName("label_2")
        self.Cancel = QtWidgets.QPushButton(Dialog)
        self.Cancel.setGeometry(QtCore.QRect(10, 210, 75, 23))
        self.Cancel.setObjectName("Cancel")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(112, 70, 151, 25))
        self.comboBox.setObjectName("comboBox")
        self.textEdit_fromDate = QtWidgets.QTextEdit(Dialog)
        self.textEdit_fromDate.setEnabled(False)
        self.textEdit_fromDate.setGeometry(QtCore.QRect(111, 113, 151, 31))
        self.textEdit_fromDate.setMouseTracking(True)
        self.textEdit_fromDate.setTabChangesFocus(True)
        self.textEdit_fromDate.setOverwriteMode(True)
        self.textEdit_fromDate.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_fromDate.setObjectName("textEdit_fromDate")
        self.textEdit_toDate = QtWidgets.QTextEdit(Dialog)
        self.textEdit_toDate.setEnabled(False)
        self.textEdit_toDate.setGeometry(QtCore.QRect(110, 163, 151, 31))
        self.textEdit_toDate.setMouseTracking(True)
        self.textEdit_toDate.setTabChangesFocus(True)
        self.textEdit_toDate.setOverwriteMode(True)
        self.textEdit_toDate.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_toDate.setObjectName("textEdit_toDate")
        self.label_fromDate = QtWidgets.QLabel(Dialog)
        self.label_fromDate.setEnabled(False)
        self.label_fromDate.setGeometry(QtCore.QRect(25, 120, 71, 16))
        self.label_fromDate.setObjectName("label_fromDate")
        self.label_toDate = QtWidgets.QLabel(Dialog)
        self.label_toDate.setEnabled(False)
        self.label_toDate.setGeometry(QtCore.QRect(40, 160, 51, 16))
        self.label_toDate.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_toDate.setObjectName("label_toDate")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(112, 23, 151, 25))
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.label.setText(_translate("Dialog", "Date"))
        self.label_2.setText(_translate("Dialog", "MMSI"))
        self.Cancel.setText(_translate("Dialog", "Cancel"))
        self.label_fromDate.setText(_translate("Dialog", "fromDate"))
        self.label_toDate.setText(_translate("Dialog", "toDate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

