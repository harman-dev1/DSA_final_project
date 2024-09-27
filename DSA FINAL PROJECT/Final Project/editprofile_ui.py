from PyQt5 import QtCore, QtGui, QtWidgets
import logo
from hashing_implementation_log_in import HashTable 
ht_instance = HashTable()
#ht_instance.load_from_file("SignUp.txt")

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
    return flag



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1091, 558)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-85, -99, 1351, 161))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 10, 151, 61))
        self.label.setStyleSheet("image: url(:/newPrefix/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(420, 90, 261, 431))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(430, 99, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(420, 120, 261, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(430, 140, 121, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(430, 170, 91, 20))
        self.label_4.setObjectName("label_4")
        self.firstnameinput = QtWidgets.QLineEdit(Dialog)
        self.firstnameinput.setGeometry(QtCore.QRect(440, 190, 231, 31))
        self.firstnameinput.setObjectName("firstnameinput")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(430, 240, 91, 20))
        self.label_5.setObjectName("label_5")
        self.lastnameinput = QtWidgets.QLineEdit(Dialog)
        self.lastnameinput.setGeometry(QtCore.QRect(440, 260, 231, 31))
        self.lastnameinput.setObjectName("lastnameinput")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(430, 310, 91, 20))
        self.label_6.setObjectName("label_6")
        self.emailinput = QtWidgets.QLineEdit(Dialog)
        self.emailinput.setGeometry(QtCore.QRect(440, 330, 231, 31))
        self.emailinput.setObjectName("emailinput")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(430, 380, 91, 20))
        self.label_7.setObjectName("label_7")
        self.passwordinput = QtWidgets.QLineEdit(Dialog)
        self.passwordinput.setGeometry(QtCore.QRect(440, 400, 231, 31))
        self.passwordinput.setObjectName("passwordinput")
        self.savebutton = QtWidgets.QPushButton(Dialog)
        self.savebutton.setGeometry(QtCore.QRect(574, 450, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.savebutton.setFont(font)
        self.savebutton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 255);")
        self.savebutton.setObjectName("savebutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.savebutton.clicked.connect(lambda: self.mainpage_ui_form(Dialog))
        self.attribute()
        
    def attribute(self):
        from mainpage_ui import first_name
        from mainpage_ui import last_name
        from mainpage_ui import email
        from mainpage_ui import password
        self.firstnameinput.setText(first_name)
        self.lastnameinput.setText(last_name)
        self.emailinput.setText(email)
        self.passwordinput.setText(str(password))
        
        
    def mainpage_ui_form(self,current_dialog):
        while True:
            entered_first_name = self.firstnameinput.text()
            entered_last_name = self.lastnameinput.text()
            entered_email = self.emailinput.text()
            entered_password = (self.passwordinput.text())
            if entered_first_name == '' or entered_last_name == '' or entered_email == '' or entered_password == 0:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                msg_box.setText("Please fill all fields!")
                msg_box.setWindowTitle("Incomplete Information")
                msg_box.exec_()
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
                msg_box.setText("Your information has been Updated!")
                msg_box.setWindowTitle("Information Stored")
                
                msg_box.exec_()
                
                
                from mainpage_ui import email
                if(ht_instance.update_user(email, entered_email, entered_first_name, entered_last_name, entered_password)) == True:
                    #ht_instance.print_hash_table()
                    print("Works correctly")
                else:
                    print("NO Working")
                self.open_start_form(current_dialog)
                break
            
                
        
      
    def open_start_form(self, current_dialog):
        from start_ui import Ui_Dialog as Start_Dialog
        self.start_form = QtWidgets.QDialog()
        self.start_ui = Start_Dialog()
        self.start_ui.setupUi(self.start_form)
        current_dialog.hide()
        self.start_form.show()
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setText("Your Have updated information Plzz Sign In to confirm!!!")
        msg_box.setWindowTitle("Information Stored")
        msg_box.exec_()
        
    #Enter from User Information 
    def update_first_name(self, text):
        self.firstnameinput = text  
    def update_last_name(self, text):
        self.lastnameinput = text
    def update_email(self, text):
        self.emailinput = text    
    def update_password(self, text):
        self.passwordinput = text 
        
        
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "  Edit Info"))
        self.label_3.setText(_translate("Dialog", "* Indicates Required"))
        self.label_4.setText(_translate("Dialog", "*  First Name:"))
        self.label_5.setText(_translate("Dialog", "*  Last Name:"))
        self.label_6.setText(_translate("Dialog", "*  Email:"))
        self.label_7.setText(_translate("Dialog", "*  Password:"))
        self.savebutton.setText(_translate("Dialog", "Save"))
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
