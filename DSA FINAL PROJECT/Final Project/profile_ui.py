import homelinkedin
import homepic
import messagepic
import networkpic
import profilepic
import updatepic
from mainpage_ui import Ui_Dialog as label
from hashing_implementation_log_in import HashTable 




#ht_instance = HashTable()
#ht_instance.load_from_file("SignUp.txt")

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1094, 561)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-5, -69, 1271, 131))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 0, 121, 61))
        self.label.setStyleSheet("image: url(:/newPrefix/homelinkedin.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.homelabel = QtWidgets.QLabel(Dialog)
        self.homelabel.setGeometry(QtCore.QRect(430, 0, 71, 61))
        self.homelabel.setStyleSheet("image: url(:/newPrefix/homepic.jpg);")
        self.homelabel.setText("")
        self.homelabel.setObjectName("homelabel")
        self.networklabel = QtWidgets.QLabel(Dialog)
        self.networklabel.setGeometry(QtCore.QRect(570, 0, 81, 61))
        self.networklabel.setStyleSheet("image: url(:/newPrefix/networkpic.jpg);")
        self.networklabel.setText("")
        self.networklabel.setObjectName("networklabel")
        self.profilelabel = QtWidgets.QLabel(Dialog)
        self.profilelabel.setGeometry(QtCore.QRect(860, 10, 111, 51))
        self.profilelabel.setStyleSheet("image: url(:/newPrefix/profilepic.jpg);")
        self.profilelabel.setText("")
        self.profilelabel.setObjectName("profilelabel")
        self.messaginglabel = QtWidgets.QLabel(Dialog)
        self.messaginglabel.setGeometry(QtCore.QRect(700, 0, 131, 61))
        self.messaginglabel.setStyleSheet("image: url(:/newPrefix/messagepic.jpg);")
        self.messaginglabel.setText("")
        self.messaginglabel.setObjectName("messaginglabel")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(430, 110, 251, 411))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.namelabel = QtWidgets.QLabel(Dialog)
        self.namelabel.setGeometry(QtCore.QRect(430, 129, 251, 41))
        self.namelabel.setObjectName("namelabel")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(470, 170, 171, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.emaillabel = QtWidgets.QLabel(Dialog)
        self.emaillabel.setGeometry(QtCore.QRect(430, 200, 251, 41))
        self.emaillabel.setObjectName("emaillabel")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(470, 240, 171, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.passwordlabel = QtWidgets.QLabel(Dialog)
        self.passwordlabel.setGeometry(QtCore.QRect(430, 270, 251, 41))
        self.passwordlabel.setObjectName("passwordlabel")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(470, 310, 171, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.updateprofilebutton = QtWidgets.QPushButton(Dialog)
        self.updateprofilebutton.setGeometry(QtCore.QRect(450, 400, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.updateprofilebutton.setFont(font)
        self.updateprofilebutton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);")
        self.updateprofilebutton.setObjectName("updateprofilebutton")
        self.updateprofilelabelpic = QtWidgets.QLabel(Dialog)
        self.updateprofilelabelpic.setGeometry(QtCore.QRect(580, 400, 101, 41))
        self.updateprofilelabelpic.setStyleSheet("image: url(:/newPrefix/updatepic.jpg);")
        self.updateprofilelabelpic.setText("")
        self.updateprofilelabelpic.setObjectName("updateprofilelabelpic")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.information_displayed()
        self.updateprofilebutton.clicked.connect(lambda:self.edit_profile(Dialog))
        self.homelabel.mousePressEvent = self.home_page
        self.messaginglabel.mousePressEvent = self.open_messaging_ui_form
        self.networklabel.mousePressEvent = self.my_network_ui_form
        
    def my_network_ui_form(self,event):
        from mynetwork_ui import Ui_Dialog as networkDialog
        self.networkform = QtWidgets.QDialog()
        self.mynetwork_ui = networkDialog()
        self.mynetwork_ui.setupUi(self.networkform)
        self.networkform.show()
    
    def edit_profile(self,current_dialog):
        from editprofile_ui import Ui_Dialog as EditprofileDialog
        self.editprofile_form = QtWidgets.QDialog()
        self.editprofile_ui = EditprofileDialog()
        self.editprofile_ui.setupUi(self.editprofile_form)
        current_dialog.hide()
        self.editprofile_form.show()
        
    def open_messaging_ui_form(self,event):
        from messaging_ui import Ui_Dialog as msgDialog
        self.msg_form = QtWidgets.QDialog()
        self.messaging_ui = msgDialog()
        self.messaging_ui.setupUi(self.msg_form)
        self.msg_form.show()
    
    def home_page(self,event):
        from mainpage_ui import Ui_Dialog as HomepageDialog
        self.home_page_form = QtWidgets.QDialog()
        self.homepage = HomepageDialog()
        self.homepage.setupUi(self.home_page_form)
        #Dialog.hide()
        self.home_page_form.show() 
        
        
    def information_displayed(self):
        from mainpage_ui import first_name
        from mainpage_ui import last_name
        from mainpage_ui import email
        from mainpage_ui import password
        print("In profile Ui" , first_name,last_name,email,password)
        name = f"<html>&nbsp;&nbsp;&nbsp;{first_name} {last_name}</html>"
        mail = f"<html>&nbsp;&nbsp;&nbsp;{email}</html>"
        epassword = f"<html>&nbsp;&nbsp;&nbsp;{password}</html>"
        self.namelabel.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.emaillabel.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.passwordlabel.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.namelabel.setText(name)
        self.emaillabel.setText(mail)
        self.passwordlabel.setText(epassword)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.namelabel.setText(_translate("Dialog", "TextLabel"))
        self.emaillabel.setText(_translate("Dialog", "TextLabel"))
        self.passwordlabel.setText(_translate("Dialog", "TextLabel"))
        self.updateprofilebutton.setText(_translate("Dialog", "Update Profile"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
