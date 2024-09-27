import logolinkedin

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

from PyQt5 import QtCore, QtGui, QtWidgets
#from hashing_implementation_log_in import HashTable 



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1077, 571)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 108);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(66, 62, 421, 351))
        self.label.setStyleSheet("image: url(:/newPrefix/logolinkedin.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.signinbutton = QtWidgets.QPushButton(Dialog)
        self.signinbutton.setGeometry(QtCore.QRect(590, 220, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signinbutton.setFont(font)
        self.signinbutton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 134);")
        self.signinbutton.setObjectName("signinbutton")
        self.signupbutton = QtWidgets.QPushButton(Dialog)
        self.signupbutton.setGeometry(QtCore.QRect(800, 220, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signupbutton.setFont(font)
        self.signupbutton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 134);")
        self.signupbutton.setObjectName("signupbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.signupbutton.clicked.connect(lambda:self.open_signup_form(Dialog)) 
        self.signinbutton.clicked.connect(lambda:self.open_signin_form(Dialog))
        
    def open_signup_form(self,current_dialog):
        from signup_ui import Ui_Dialog as SignupDialog
        self.signup_form = QtWidgets.QDialog()
        self.signup_ui = SignupDialog()
        self.signup_ui.setupUi(self.signup_form)
        current_dialog.hide()
        self.signup_form.show()
    
    def open_signin_form(self,current_dialog):
        from signin_ui import Ui_Dialog as SigninDialog
        self.signin_form = QtWidgets.QDialog()
        self.signin_ui = SigninDialog()
        self.signin_ui.setupUi(self.signin_form)
        current_dialog.hide()
        self.signin_form.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.signinbutton.setText(_translate("Dialog", "Sign In"))
        self.signupbutton.setText(_translate("Dialog", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
