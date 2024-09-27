from PyQt5 import QtCore, QtGui, QtWidgets
from hashing_implementation_log_in import HashTable 

ht_instance = HashTable()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(782, 581)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-35, -19, 891, 691))
        self.graphicsView.setStyleSheet("background-color: rgb(0, 0, 48);")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 70, 280, 430))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/photos/LOGO LINKEDIN.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.signupbutton = QtWidgets.QPushButton(Dialog)
        self.signupbutton.setGeometry(QtCore.QRect(430, 250, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signupbutton.setFont(font)
        self.signupbutton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"\n"
"color: rgb(117, 0, 0);")
        self.signupbutton.setObjectName("signupbutton")
        self.signinbutton = QtWidgets.QPushButton(Dialog)
        self.signinbutton.setGeometry(QtCore.QRect(600, 250, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signinbutton.setFont(font)
        self.signinbutton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"\n"
"color: rgb(117, 0, 0);")
        self.signinbutton.setObjectName("signinbutton")

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
        self.signupbutton.setText(_translate("Dialog", "Sign Up"))
        self.signinbutton.setText(_translate("Dialog", "Sign In"))

ht_instance.load_from_file('SignUp.txt')
ht_instance.print_hash_table()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())