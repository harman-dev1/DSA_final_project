from hashing_implementation_log_in import HashTable 
from PyQt5 import QtCore, QtGui, QtWidgets
import logo
from for_requests import LinkedList
from mynetwork_ui import Ui_Dialog as s_profile

from graphs_implementation import Graph
g1 = Graph()
ht_instance = HashTable()
ht_instance.load_from_file("SignUp.txt")


#l1.load_from_file("Pending_Requests.txt")

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1091, 562)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-105, 0, 1361, 71))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 10, 161, 71))
        self.label.setStyleSheet("image: url(:/newPrefix/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(440, 120, 221, 361))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(456, 140, 61, 20))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.namelabl = QtWidgets.QLabel(Dialog)
        self.namelabl.setGeometry(QtCore.QRect(466, 169, 161, 31))
        self.namelabl.setObjectName("namelabl")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(460, 190, 161, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.emaillabel = QtWidgets.QLabel(Dialog)
        self.emaillabel.setGeometry(QtCore.QRect(460, 230, 161, 31))
        self.emaillabel.setObjectName("emaillabel")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(460, 250, 161, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.connectbutoon = QtWidgets.QPushButton(Dialog)
        self.connectbutoon.setGeometry(QtCore.QRect(560, 320, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.connectbutoon.setFont(font)
        self.connectbutoon.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.connectbutoon.setObjectName("connectbutoon")
        self.messagebutton = QtWidgets.QPushButton(Dialog)
        self.messagebutton.setGeometry(QtCore.QRect(450, 320, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.messagebutton.setFont(font)
        self.messagebutton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.messagebutton.setObjectName("messagebutton")
        self.previousbutton = QtWidgets.QPushButton(Dialog)
        self.previousbutton.setGeometry(QtCore.QRect(510, 380, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.previousbutton.setFont(font)
        self.previousbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.previousbutton.setObjectName("previousbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.messagebutton.clicked.connect(lambda:self.open_messaging_ui_form(Dialog))
        self.previousbutton.clicked.connect(lambda: self.home_page(Dialog))
        self.connectbutoon.clicked.connect(lambda:self.connection_msg(Dialog))
        from mainpage_ui import found_user
        self.namelabl.setText(found_user.first_name+ " " + found_user.last_name)
        self.emaillabel.setText(found_user.email) 
    def connection_msg(self,current_dialog):
        from mainpage_ui import found_user
        from mainpage_ui import email
        
        from for_requests import LinkedList
        l1 = LinkedList()
        l1.load_from_file("Friend_Requests.txt")
        print("In Msg BOX")
        l1.print_node()
        
        if g1.check_already_friend(email, found_user.email) == True:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Information)
            msg_box.setText("You are Already Connected To this User!!!")
            msg_box.setWindowTitle("Already")
            msg_box.exec_()
            
        elif l1.already_sent_connection(email, found_user.email):
            l1.save_to_file("Pending_Requests.txt")
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Information)
            msg_box.setText("Connection is Sent Already!!!")
            msg_box.setWindowTitle("Sent")
            msg_box.exec_()
            
            
        else:
            s_profile.users_pending_connection(self,found_user)
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Information)
            msg_box.setText("Connection Sent Succsessfully!!!")
            msg_box.setWindowTitle("Sent")
            msg_box.exec_()
            
    def open_messaging_ui_form(self,current_dialog):
        from messaging_ui import Ui_Dialog as msgDialog
        self.msg_form = QtWidgets.QDialog()
        self.messaging_ui = msgDialog()
        self.messaging_ui.setupUi(self.msg_form)
        current_dialog.hide()
        self.msg_form.show()
        
    def home_page(self,current_dialog):
        from mainpage_ui import Ui_Dialog as HomepageDialog
        self.home_page_form = QtWidgets.QDialog()
        self.homepage = HomepageDialog()
        self.homepage.setupUi(self.home_page_form)
        current_dialog.hide()
        self.home_page_form.show()
        
    def attribute(self, found_node):
        global first_name, last_name, email, password
        first_name = found_node.first_name
        last_name = found_node.last_name
        email = found_node.email
        password = found_node.password
        
           

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.namelabl.setText(_translate("Dialog", "TextLabel"))
        self.emaillabel.setText(_translate("Dialog", "TextLabel"))
        self.connectbutoon.setText(_translate("Dialog", "Connect"))
        self.messagebutton.setText(_translate("Dialog", "Message"))
        self.previousbutton.setText(_translate("Dialog", "Previous"))

first_name = ""
last_name = ""
email = ""
password = 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
