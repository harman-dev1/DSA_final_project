import homelinkedin
import homepic
import logo
import logolinkedin
import messagepic
import networkpic
import picformessage
import profilepic


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication, QMessageBox
from graphs_implementation import Graph
g1 = Graph()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 559)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-95, -109, 1351, 171))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 0, 91, 61))
        self.label.setStyleSheet("image: url(:/newPrefix/homelinkedin.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.homelabel = QtWidgets.QLabel(Dialog)
        self.homelabel.setGeometry(QtCore.QRect(426, 2, 71, 61))
        self.homelabel.setStyleSheet("image: url(:/newPrefix/homepic.jpg);")
        self.homelabel.setText("")
        self.homelabel.setObjectName("homelabel")
        self.networklabel = QtWidgets.QLabel(Dialog)
        self.networklabel.setGeometry(QtCore.QRect(560, 0, 81, 61))
        self.networklabel.setStyleSheet("image: url(:/newPrefix/networkpic.jpg);")
        self.networklabel.setText("")
        self.networklabel.setObjectName("networklabel")
        self.messaginlabel = QtWidgets.QLabel(Dialog)
        self.messaginlabel.setGeometry(QtCore.QRect(700, 0, 81, 61))
        self.messaginlabel.setStyleSheet("image: url(:/newPrefix/messagepic.jpg);")
        self.messaginlabel.setText("")
        self.messaginlabel.setObjectName("messaginlabel")
        self.profilelabel = QtWidgets.QLabel(Dialog)
        self.profilelabel.setGeometry(QtCore.QRect(840, 0, 81, 61))
        self.profilelabel.setStyleSheet("image: url(:/newPrefix/profilepic.jpg);")
        self.profilelabel.setText("")
        self.profilelabel.setObjectName("profilelabel")
        self.friendstable = QtWidgets.QTableWidget(Dialog)
        self.friendstable.setGeometry(QtCore.QRect(140, 200, 211, 291))
        self.friendstable.setStyleSheet("")
        self.friendstable.setLineWidth(2)
        self.friendstable.setShowGrid(True)
        self.friendstable.setGridStyle(QtCore.Qt.DashDotLine)
        self.friendstable.setRowCount(1000)
        self.friendstable.setObjectName("friendstable")
        self.friendstable.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.friendstable.setHorizontalHeaderItem(0, item)
        self.friendstable.horizontalHeader().setDefaultSectionSize(160)
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(140, 80, 211, 121))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.searchbar = QtWidgets.QLineEdit(Dialog)
        self.searchbar.setGeometry(QtCore.QRect(160, 140, 171, 31))
        self.searchbar.setObjectName("searchbar")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(450, 70, 571, 351))
        self.label_6.setStyleSheet("image: url(:/newPrefix/picformessageui.jpg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.profilelabel.mousePressEvent = self.open_profile_ui_form
        self.homelabel.mousePressEvent = self.home_page
        self.networklabel.mousePressEvent = self.my_network_ui_form
        
        self.searchbar.textChanged.connect(self.filter_friends_table)
        self.friendstable.cellClicked.connect(self.messaging_form)
           
        from mainpage_ui import email
        list_of_friends = g1.all_friends_of_login_user(email)
        print(list_of_friends)
        self.friendstable.setRowCount(len(list_of_friends))
        for idx, friend_name in enumerate(list_of_friends):
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(friend_name)) 
            self.friendstable.setItem(idx, 0, item) 
            
    def filter_friends_table(self, text):
        search_text = self.searchbar.text().lower()
        for row in range(self.friendstable.rowCount()):
            item = self.friendstable.item(row, 0)
            if item is not None:
                friend_name = item.text().lower()
                self.friendstable.setRowHidden(row, search_text not in friend_name)
    
    def messaging_form(self,event):
        selected_user = self.friendstable.currentItem().text()
        
        from sendmessage_ui import Ui_Dialog as sendDialog
        self.sendmessageform = QtWidgets.QDialog()
        self.sendmessage_ui = sendDialog()
        self.sendmessage_ui.setupUi(self.sendmessageform, selected_user)
        self.sendmessageform.show()
    
    def my_network_ui_form(self,event):
        from mynetwork_ui import Ui_Dialog as networkDialog
        self.networkform = QtWidgets.QDialog()
        self.mynetwork_ui = networkDialog()
        self.mynetwork_ui.setupUi(self.networkform)
        self.networkform.show()
        
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
        
    def open_profile_ui_form(self,event):
        from profile_ui import Ui_Dialog as SigninDialog
        self.profile_form = QtWidgets.QDialog()
        self.profile_ui = SigninDialog()
        self.profile_ui.setupUi(self.profile_form)
        self.profile_form.show()
        #self.Dialog.hide()
    
    def home_page(self,event):
        from mainpage_ui import Ui_Dialog as HomepageDialog
        self.home_page_form = QtWidgets.QDialog()
        self.homepage = HomepageDialog()
        self.homepage.setupUi(self.home_page_form)
        #Dialog.hide()
        self.home_page_form.show() 

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.friendstable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Friends"))
        self.searchbar.setPlaceholderText(_translate("Dialog", " Search Messages"))
        self.pushButton.setText(_translate("Dialog", "Message Friends"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
