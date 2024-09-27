import extrapic
import homelinkedin
import homepic
import messagepic
import networkpic
import profilepic
import profilepicforpost
import startpost
from PyQt5 import QtCore, QtGui, QtWidgets
from hashing_implementation_log_in import HashTable 
from searchprofile_ui import Ui_Dialog as conectionDialog
from PyQt5.QtWidgets import QDialog,QApplication, QMessageBox

found_user = None

ht_instance = HashTable()
#ht_instance.load_from_file("SignUp.txt")

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1087, 559)
        Dialog.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1050, 1218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(100, 1200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(-195, -89, 1361, 141))
        self.graphicsView.setObjectName("graphicsView")
        self.searchbar = QtWidgets.QLineEdit(self.frame)
        self.searchbar.setGeometry(QtCore.QRect(110, 10, 221, 31))
        self.searchbar.setObjectName("searchbar")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, -5, 71, 61))
        self.label.setStyleSheet("image: url(:/newPrefix/homelinkedin.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.networklabel = QtWidgets.QLabel(self.frame)
        self.networklabel.setGeometry(QtCore.QRect(550, 0, 81, 51))
        self.networklabel.setStyleSheet("image: url(:/newPrefix/networkpic.jpg);")
        self.networklabel.setText("")
        self.networklabel.setObjectName("networklabel")
        self.messaginglabel = QtWidgets.QLabel(self.frame)
        self.messaginglabel.setGeometry(QtCore.QRect(700, 0, 91, 51))
        self.messaginglabel.setStyleSheet("image: url(:/newPrefix/messagepic.jpg);")
        self.messaginglabel.setText("")
        self.messaginglabel.setObjectName("messaginglabel")
        self.profilelabel = QtWidgets.QLabel(self.frame)
        self.profilelabel.setGeometry(QtCore.QRect(830, 0, 101, 51))
        self.profilelabel.setStyleSheet("image: url(:/newPrefix/profilepic.jpg);")
        self.profilelabel.setText("")
        self.profilelabel.setObjectName("profilelabel")
        
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_2.setGeometry(QtCore.QRect(235, 70, 561, 71))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_2.setVisible(False)  # Hide the graphicsView_2 widget

        # Hide labels associated with graphicsView_2
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(256, 82, 61, 51))
        self.label_6.setStyleSheet("image: url(:/newPrefix/profilepicforpost.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_6.setVisible(False)  # Hide label_6
        self.startpostlabel = QtWidgets.QLabel(self.frame)
        self.startpostlabel.setGeometry(QtCore.QRect(320, 80, 431, 51))
        self.startpostlabel.setStyleSheet("image: url(:/newPrefix/startpost.jpg);")
        self.startpostlabel.setText("")
        self.startpostlabel.setObjectName("startpostlabel")
        self.startpostlabel.setVisible(False)
        
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(770, 150, 251, 301))
        self.label_8.setStyleSheet("image: url(:/newPrefix/extrapic.jpg);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_3.setGeometry(QtCore.QRect(50, 100, 141, 281))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(50, 150, 141, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(76, 112, 81, 61))
        self.label_9.setStyleSheet("image: url(:/newPrefix/profilepic.jpg);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.profilebutton = QtWidgets.QLabel(self.frame)
        self.profilebutton.setGeometry(QtCore.QRect(50, 180, 131, 41))
        self.profilebutton.setObjectName("profilebutton")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(50, 310, 141, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.discoverlabel = QtWidgets.QLabel(self.frame)
        self.discoverlabel.setGeometry(QtCore.QRect(50, 320, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.discoverlabel.setFont(font)
        self.discoverlabel.setObjectName("discoverlabel")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(60, 220, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(430, 0, 81, 51))
        self.label_2.setStyleSheet("image: url(:/newPrefix/homepic.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.change_profile_button_text()
        
        self.searchbar.returnPressed.connect(self.on_search)
        
       #...................
        self.profilebutton.mousePressEvent = self.open_profile_ui_form
        self.label_9.mousePressEvent = self.open_profile_ui_form
        self.profilelabel.mousePressEvent = self.open_start_form
        self.messaginglabel.mousePressEvent = self.open_messaging_ui_form
        self.networklabel.mousePressEvent = self.my_network_ui_form
        self.discoverlabel.mousePressEvent = self.my_network_ui_form
       #
     
    def on_search(self):
        email = self.searchbar.text()
        if email:
            global found_user 
            found_user = ht_instance.user_for_searching(email)
            
            if found_user == "Same":
                self.open_profile_ui_form(None)
            if found_user != "Same" and found_user != "Not Found":
                self.search_profile_ui_form()
            if found_user ==  "Not Found":
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                msg_box.setText("User Not Found 404 !!!")
                msg_box.setWindowTitle("Not Found")
                self.searchbar.clear()
                msg_box.exec_()
                     
    def search_profile_ui_form(self):
        from searchprofile_ui import Ui_Dialog as conectionDialog
        self.connectionform = QtWidgets.QDialog()
        self.searchprofile_ui = conectionDialog()
        self.searchprofile_ui.setupUi(self.connectionform)
        self.connectionform.show()
                
    def open_profile_ui_form(self,event):
        from profile_ui import Ui_Dialog as SigninDialog
        self.profile_form = QtWidgets.QDialog()
        self.profile_ui = SigninDialog()
        self.profile_ui.setupUi(self.profile_form)
        self.profile_form.show()
        #self.Dialog.hide()
        
    def open_messaging_ui_form(self,event):
        from messaging_ui import Ui_Dialog as msgDialog
        self.msg_form = QtWidgets.QDialog()
        self.messaging_ui = msgDialog()
        self.messaging_ui.setupUi(self.msg_form)
        self.msg_form.show()
        
    
    def my_network_ui_form(self,event):
        print("In Network Form--------------")
        from mynetwork_ui import Ui_Dialog as networkDialog
        self.networkform = QtWidgets.QDialog()
        self.mynetwork_ui = networkDialog()
        self.mynetwork_ui.setupUi(self.networkform)
        self.networkform.show()
    #...................
    
    def open_start_form(self, event):
        reply = QMessageBox.question(None, 'Logout Confirmation', 'Are you sure you want to log out?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            from start_ui import Ui_Dialog as Start_Dialog
            self.start_form = QtWidgets.QDialog()
            self.start_ui = Start_Dialog()
            self.start_ui.setupUi(self.start_form)
            self.start_form.show()
        else:
            pass  
     
    def attribute(self, found_node):
        global first_name, last_name, email, password
        first_name = found_node.first_name
        last_name = found_node.last_name
        email = found_node.email
        password = found_node.password
        conectionDialog.attribute(self, found_node)
                
        
    def change_profile_button_text(self):
        text = f"<html>&nbsp;&nbsp;&nbsp;{first_name} {last_name}</html>"
        self.profilebutton.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.profilebutton.setText(text)  
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.searchbar.setPlaceholderText(_translate("Dialog", "   Search"))
        self.profilebutton.setText(_translate("Dialog", "     TextLabel"))
        self.discoverlabel.setText(_translate("Dialog", "  Discover More"))


first_name = ""
last_name = ""
email = ""
password = 0
#ht_instance.load_from_file("SignUp.txt")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
