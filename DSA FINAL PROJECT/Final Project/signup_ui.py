import logo
from PyQt5 import QtCore, QtGui, QtWidgets
#from start_ui import Ui_Dialog as Start_Dialog
from PyQt5.QtWidgets import QDialog,QApplication, QMessageBox
from hashing_implementation_log_in import HashTable 

#validations

def check_email(email):
    mail = ['@', 'g', 'm', 'a', 'i', 'l', '.', 'c', 'o', 'm']
    length_of_email = len(email) - 11
    count_email = len(email) - 1

    i = 9
    flag = False
    while count_email != length_of_email:
        if email[count_email] == mail[i] and email[0] != mail[0]:
            flag = True
        else:
            flag = False
            break
        count_email -= 1
        i -= 1
    if '-' in email:
        flag = False
        
    return flag

first_name = ""
last_name = ""
email = ""
email_password = 0

# driver code for UI 
class Ui_Dialog(object):
    current_id = 0
    def setupUi(self, Dialog):
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(786, 584)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-20, -40, 911, 691))
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 201, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/photos/logo.png"))
        self.label_2.setObjectName("label_2")
        self.signinbutton_2 = QtWidgets.QPushButton(Dialog)
        self.signinbutton_2.setGeometry(QtCore.QRect(270, 50, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signinbutton_2.setFont(font)
        self.signinbutton_2.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.signinbutton_2.setObjectName("signinbutton_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(270, 120, 301, 431))
        self.graphicsView_2.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(280, 160, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_4.setObjectName("label_4")
        self.firstnameinput = QtWidgets.QLineEdit(Dialog)
        self.firstnameinput.setGeometry(QtCore.QRect(290, 180, 241, 31))
        self.firstnameinput.setObjectName("firstnameinput")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(280, 220, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_5.setObjectName("label_5")
        self.lastnameinput = QtWidgets.QLineEdit(Dialog)
        self.lastnameinput.setGeometry(QtCore.QRect(290, 240, 241, 31))
        self.lastnameinput.setObjectName("lastnameinput")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(280, 280, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_3.setObjectName("label_3")
        self.emailinput = QtWidgets.QLineEdit(Dialog)
        self.emailinput.setGeometry(QtCore.QRect(290, 300, 241, 31))
        self.emailinput.setObjectName("emailinput")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(280, 340, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_6.setObjectName("label_6")
        self.passwordinput = QtWidgets.QLineEdit(Dialog)
        self.passwordinput.setGeometry(QtCore.QRect(290, 360, 241, 31))
        self.passwordinput.setObjectName("passwordinput")
        self.continuebutton = QtWidgets.QPushButton(Dialog)
        self.continuebutton.setGeometry(QtCore.QRect(310, 400, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.continuebutton.setFont(font)
        self.continuebutton.setStyleSheet("background-color: rgb(232, 232, 232);color: rgb(0, 0, 255);")
        self.continuebutton.setObjectName("continuebutton")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(300, 450, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_7.setObjectName("label_7")
        self.signinbutton = QtWidgets.QPushButton(Dialog)
        self.signinbutton.setGeometry(QtCore.QRect(450, 450, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signinbutton.setFont(font)
        self.signinbutton.setStyleSheet("background-color: rgb(232, 232, 232);color: rgb(0, 0, 255);")
        self.signinbutton.setObjectName("signinbutton")
        
        
        self.firstnameinput.textChanged.connect(self.update_first_name)
        self.lastnameinput.textChanged.connect(self.update_last_name)
        self.emailinput.textChanged.connect(self.update_email)
        self.passwordinput.textChanged.connect(self.update_password)
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.signinbutton.clicked.connect(lambda:self.open_signin_form(Dialog))
        self.continuebutton.clicked.connect(lambda: self.display_message(Dialog))
            
    def display_message(self,current_dialog):
        ht_instance = HashTable()
        ht_instance.load_from_file("SignUp.txt")
        while True:
           entered_first_name = self.firstnameinput.text()
           entered_last_name = self.lastnameinput.text()
           entered_email = self.emailinput.text()
           entered_password = (self.passwordinput.text())
           if entered_first_name == '' or entered_last_name == '' or entered_email == '' or entered_password == '':
               msg_box = QtWidgets.QMessageBox()
               msg_box.setIcon(QtWidgets.QMessageBox.Warning)
               msg_box.setText("Please fill all fields!")
               msg_box.setWindowTitle("Incomplete Information")
               msg_box.exec_()
               break
           
           if not ht_instance.unique_email(entered_email):
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                msg_box.setText("Email already exists! Please use a different email.")
                msg_box.setWindowTitle("Existing Email")
                msg_box.exec_()
                self.emailinput.clear()
                break 
           if not check_email(entered_email):
               entered_email, ok = QtWidgets.QInputDialog.getText(None, "Invalid Email", "Please enter a valid email:")
               if not ok:
                   break 
               self.emailinput.setText(entered_email)
               continue
           
            
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
               
               
           if len(entered_password) > 10:
               msg_box = QtWidgets.QMessageBox()
               msg_box.setIcon(QtWidgets.QMessageBox.Warning)
               msg_box.setText("Password length must not exceed 10 characters!")
               msg_box.setWindowTitle("Invalid Password Length")
               self.passwordinput.clear()
               msg_box.exec_()
               break  
           else:
               msg_box = QtWidgets.QMessageBox()
               msg_box.setIcon(QtWidgets.QMessageBox.Information)
               msg_box.setText("Your information has been stored successfully!")
               msg_box.setWindowTitle("Information Stored")
               msg_box.exec_()
               self.firstnameinput.clear()
               self.lastnameinput.clear()
               self.emailinput.clear()
               self.passwordinput.clear()
               self.open_start_form(current_dialog)
               if self.email_password != '':
                   int_password = int(self.email_password)
                   print(first_name)   
               ht_instance.insert(entered_first_name, entered_last_name, entered_email, int(entered_password))
               ht_instance.print_hash_table()
               
               break
            
    def open_start_form(self, current_dialog):
        from start_ui import Ui_Dialog as Start_Dialog
        self.start_form = QtWidgets.QDialog()
        self.start_ui = Start_Dialog()
        self.start_ui.setupUi(self.start_form)
        current_dialog.hide()
        self.start_form.show()
        
        
    #Enter from User Information 
    def update_first_name(self, text):
        self.first_name = text  
    def update_last_name(self, text):
        self.last_name = text
    def update_email(self, text):
        self.email = text    
    def update_password(self, text):
        self.email_password = text   
        
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
        self.signinbutton_2.setText(_translate("Dialog", "Sign Up"))
        self.label_4.setText(_translate("Dialog", "   First Name:"))
        self.label_5.setText(_translate("Dialog", "   Last Name:"))
        self.label_3.setText(_translate("Dialog", "   Email:"))
        self.label_6.setText(_translate("Dialog", "   Password:"))
        self.continuebutton.setText(_translate("Dialog", "Continue"))
        self.label_7.setText(_translate("Dialog", "Already Have Account!"))
        self.signinbutton.setText(_translate("Dialog", "Sign In"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())