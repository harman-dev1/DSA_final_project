import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication, QMessageBox
from PyQt5.uic import loadUi

account_file = "E:\\DSA\\Final Project\\datafile.txt"

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("E:\\DSA\\Final Project\\start.ui",self)
        self.signinbutton.clicked.connect(self.gotosignin)
        self.signupbutton.clicked.connect(self.gotosignup)

    def gotosignin(self):
        signin = SignIn()
        widget.addWidget(signin)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotosignup(self):
        signup = SignUp()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)    


class SignIn(QDialog):
        def __init__(self):
            super(SignIn,self).__init__()
            loadUi("E:\\DSA\\Final Project\\signin.ui",self)
            self.continuebutton.clicked.connect(self.loginfunction)
            self.passwordinput.setEchoMode(QtWidgets.QLineEdit.Password)

            def loginfunction(self):
                email = self.emailinput.text()
                password = self.passwordinput.text()  

                if not email or not password:
                    QMessageBox.critical(self, "Error", "Please fill in both email and password fields.")
                    return

            # Check if the email and password match any account in the file

                if not os.path.exists(account_file):
                    QMessageBox.critical(self, "Error", "Account file does not exist. Please create an account first.")
                    return           

                with open(account_file, "r") as file:
                    for line in file:
                        stored_data = line.strip().split(',')
                        stored_email, stored_password = stored_data[2], stored_data[3]  # Assuming email is at index 2 and password is at index 3
                        if email == stored_email and password == stored_password:
                        # Login successful, you can open the main UI form here

                            QMessageBox.information(self, "Success", "Login Successful")



class SignUp(QDialog):
        def __init__(self):
            super(SignIn,self).__init__()
            loadUi("E:\\DSA\\Final Project\\signup.ui",self)
            self.continuebutton.clicked.connect(self.createaccount)
            self.password.setEchoMode(QtWidgets.QLineEdit.Password) 

            def createaccount(self):
            
                firstname = self.firstnameinput.text()
                lastname= self.lastnameinput.text()
                email = self.emailinput.text()
                password = self.passwordinput.text()
                if not email or not password:
                    QMessageBox.critical(self, "Error", "Please fill in all fields.")
                    return
                 
                with open(account_file, "a") as file:
                    file.write(f"{firstname},{lastname},{email},{password}\n")

                QMessageBox.information(self, "Success", "Account created successfully.") 
                login = Login()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex() + 1)      
 


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(691)
widget.setFixedWidth(871)
widget.show()
app.exec_()