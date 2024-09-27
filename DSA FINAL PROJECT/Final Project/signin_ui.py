from PyQt5 import QtCore, QtGui, QtWidgets
from hashing_implementation_log_in import HashTable 
from mainpage_ui import Ui_Dialog as label
from editprofile_ui import Ui_Dialog as assign

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(786, 668)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-45, -60, 881, 791))
        self.graphicsView.setObjectName("graphicsView")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 201, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/photos/logo.png"))
        self.label_4.setObjectName("label_4")
        self.signinbutton_2 = QtWidgets.QPushButton(Dialog)
        self.signinbutton_2.setGeometry(QtCore.QRect(230, 90, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signinbutton_2.setFont(font)
        self.signinbutton_2.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.signinbutton_2.setObjectName("signinbutton_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(230, 170, 301, 371))
        self.graphicsView_2.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 210, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_3.setObjectName("label_3")
        self.emailinput = QtWidgets.QLineEdit(Dialog)
        self.emailinput.setGeometry(QtCore.QRect(260, 230, 241, 31))
        self.emailinput.setObjectName("emailinput")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(250, 270, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_6.setObjectName("label_6")
        self.passwordinput = QtWidgets.QLineEdit(Dialog)
        self.passwordinput.setGeometry(QtCore.QRect(260, 290, 241, 31))
        self.passwordinput.setObjectName("passwordinput")
        self.continuebutton = QtWidgets.QPushButton(Dialog)
        self.continuebutton.setGeometry(QtCore.QRect(270, 340, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.continuebutton.setFont(font)
        self.continuebutton.setStyleSheet("background-color: rgb(232, 232, 232);color: rgb(0, 0, 255);")
        self.continuebutton.setObjectName("continuebutton")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(260, 400, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_7.setObjectName("label_7")
        self.signupbutton = QtWidgets.QPushButton(Dialog)
        self.signupbutton.setGeometry(QtCore.QRect(410, 400, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signupbutton.setFont(font)
        self.signupbutton.setStyleSheet("background-color: rgb(232, 232, 232);color: rgb(0, 0, 255);")
        self.signupbutton.setObjectName("signupbutton")        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.signupbutton.clicked.connect(lambda:self.open_signup_form(Dialog)) 
        self.continuebutton.clicked.connect(lambda:self.display_message(Dialog))
    
    
    def display_message(self,current_dialog):
        ht_instance = HashTable()
        while True:
            entered_email = self.emailinput.text()
            entered_password = self.passwordinput.text()
            if entered_email == '' or entered_password == '':
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                msg_box.setText("Please fill all fields!")
                msg_box.setWindowTitle("Incomplete Information")
                msg_box.exec_()
                break
            if entered_password.startswith('-') :
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                msg_box.setText("Password must be positive!")
                msg_box.setWindowTitle("Invalid Password")
                self.passwordinput.clear()
                msg_box.exec_()
                return
            
            if not entered_password.isdigit():
             msg_box = QtWidgets.QMessageBox()
             msg_box.setIcon(QtWidgets.QMessageBox.Warning)
             msg_box.setText("Password should only contain numbers!")
             msg_box.setWindowTitle("Invalid Password")
             msg_box.exec_()
             self.passwordinput.clear()
             break
            
            if ht_instance.search(int(entered_password), entered_email):
                found_node = ht_instance.search(int(entered_password), entered_email)
                label.attribute(self,found_node)
                self.home_page(current_dialog)
                break
            else:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                msg_box.setText("Incorrect email or password. Please try again!!!")
                msg_box.setWindowTitle("Incorrect Information")
                msg_box.exec_()
                self.emailinput.clear()
                self.passwordinput.clear()
                break    
    def home_page(self,current_dialog):
        from mainpage_ui import Ui_Dialog as HomepageDialog
        self.home_page_form = QtWidgets.QDialog()
        self.homepage = HomepageDialog()
        self.homepage.setupUi(self.home_page_form)
        current_dialog.hide()
        self.home_page_form.show()        
    def open_signup_form(self,current_dialog):
        from signup_ui import Ui_Dialog as SignupDialog
        self.signup_form = QtWidgets.QDialog()
        self.signup_ui = SignupDialog()
        self.signup_ui.setupUi(self.signup_form)
        current_dialog.hide()
        self.signup_form.show()   

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.signinbutton_2.setText(_translate("Dialog", "Sign In"))
        self.label_3.setText(_translate("Dialog", "   Email:"))
        self.label_6.setText(_translate("Dialog", "   Password:"))
        self.continuebutton.setText(_translate("Dialog", "Continue"))
        self.label_7.setText(_translate("Dialog", "Don\'t Have Any Account!"))
        self.signupbutton.setText(_translate("Dialog", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
