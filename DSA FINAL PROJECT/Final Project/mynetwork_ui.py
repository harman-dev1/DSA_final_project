from PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets

from for_requests import LinkedList
from graphs_implementation import Graph
g1 = Graph()
g1.load_from_file("Friends_connection.txt")
print("Loading Printing Graph")
g1.print_graph()
l1 = LinkedList()
l1.load_from_file("Pending_Requests.txt")


class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal(int)  # Signal now accepts an integer parameter

    def __init__(self, text, row, parent=None):
        super(ClickableLabel, self).__init__(text, parent)
        self.row = row
        self.setStyleSheet("border: 1px solid black;")
        self.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        self.clicked.emit(self.row)



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1109, 575)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-90, -90, 1361, 151))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, -5, 101, 71))
        self.label.setStyleSheet("image: url(:/newPrefix/homelinkedin.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 0, 71, 61))
        self.label_2.setStyleSheet("image: url(:/newPrefix/homepic.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(510, 0, 91, 61))
        self.label_3.setStyleSheet("image: url(:/newPrefix/networkpic.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(680, 0, 91, 61))
        self.label_4.setStyleSheet("image: url(:/newPrefix/messagepic.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(860, 0, 81, 61))
        self.label_5.setStyleSheet("image: url(:/newPrefix/profilepic.jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(210, 130, 661, 141))
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(210, 90, 661, 41))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(390, 90, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_6.setObjectName("label_6")
        
        self.graphicsView_3 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_3.setGeometry(QtCore.QRect(210, 290, 661, 41))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_3.setVisible(False)  # Hide graphicsView_3
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(360, 290, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_7.setObjectName("label_7")
        self.label_7.setVisible(False)  # Hide label_7
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(210, 330, 661, 141))
        self.tableWidget_2.setRowCount(1000)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(303)
        self.tableWidget_2.setVisible(False)
        
        
        
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.label_4.mousePressEvent = self.open_messaging_ui_form
        self.label_5.mousePressEvent = self.open_profile_ui_form
        self.label_2.mousePressEvent = self.home_page
        
        from mainpage_ui import first_name
        from mainpage_ui import last_name
        from mainpage_ui import email
        from mainpage_ui import password
        from mainpage_ui import found_user
        connection_of_friends_to_be_displayed = l1.email_to_be_displayed(email)
        for row, email in enumerate(connection_of_friends_to_be_displayed):
            email_item = QtWidgets.QTableWidgetItem(email)
            self.tableWidget.setItem(row, 0, email_item)
    
        
  #Displaying in Friend Table
        for row in range(1000):
            accept_label = ClickableLabel("Accept", row)
            accept_label.setAlignment(Qt.AlignCenter)
            self.tableWidget.setCellWidget(row, 1, accept_label)
            accept_label.clicked.connect(lambda row=row: self.accept_clicked(row))

            ignore_label = ClickableLabel("Ignore", row)
            ignore_label.setAlignment(Qt.AlignCenter)
            self.tableWidget.setCellWidget(row, 2, ignore_label)
            ignore_label.clicked.connect(lambda row=row: self.ignore_clicked(row))

            
        
    def users_pending_connection(self,found_user):
        #l1.load_from_file("Pending_Requests.txt")
        from mainpage_ui import first_name
        from mainpage_ui import last_name
        from mainpage_ui import email
        from mainpage_ui import password
        global first_name_of_f,last_name_of_f,email_of_f,password_of_f
        first_name_of_f = found_user.first_name
        last_name_of_f = found_user.last_name
        email_of_f = found_user.email
        password_of_f = found_user.password
        l1.insert_node_at_end(first_name,last_name,email,password,found_user.first_name,found_user.last_name,found_user.email,found_user.password)
        l1.print_node()
        l1.save_to_file("Pending_Requests.txt")
        
    def accept_clicked(self, row): 
        from hashing_implementation_log_in import HashTable
        ht_instance = HashTable()
        ht_instance.load_from_file("SignUp.txt")
        email_item = self.tableWidget.item(row, 0)
        if email_item:
            email_address = email_item.text()
            if(email_address != ""):
                found_user = ht_instance.user_for_searching(email_address)
            from mainpage_ui import first_name
            from mainpage_ui import last_name
            from mainpage_ui import email
            from mainpage_ui import password
            found_login_user = ht_instance.user_for_searching(email)
            l1.made_friend_None_connection(email, found_user.email)
            print("For Graph Values:")
            g1.add_edge(first_name,last_name,email,password,found_user.first_name,found_user.last_name,found_user.email,found_user.password)
            g1.add_edge(found_user.first_name,found_user.last_name,found_user.email,found_user.password,first_name,last_name,email,password)
            g1.print_graph()
            accept_label = self.tableWidget.cellWidget(row, 1)
            accept_label.setText("You are now friends")

            ignore_label = self.tableWidget.cellWidget(row, 2)
            if ignore_label:
                self.tableWidget.removeCellWidget(row, 2)    
        
    def ignore_clicked(self, row):
        from hashing_implementation_log_in import HashTable
        ht_instance = HashTable()
        ht_instance.load_from_file("SignUp.txt")
        email_item = self.tableWidget.item(row, 0)
        if email_item:
            email_address = email_item.text()
            if email_address != "":
                found_user = ht_instance.user_for_searching(email_address)
            from mainpage_ui import email
            l1.made_friend_None_connection(email, found_user.email)
            
            accept_label = self.tableWidget.cellWidget(row, 1)
            if accept_label:
                accept_label.setText("")

            ignore_label = self.tableWidget.cellWidget(row, 2)
            if ignore_label:
                ignore_label.setText("You removed connection")

    def connect_clicked(self, event, row, label):
        label.setText("Connected")
        
        self.label_2.mousePressEvent = self.home_page
        self.label_4.mousePressEvent = self.open_messaging_ui_form        
        self.label_5.mousePressEvent = self.open_profile_ui_form
    
    def home_page(self,event):
        from mainpage_ui import Ui_Dialog as HomepageDialog
        self.home_page_form = QtWidgets.QDialog()
        self.homepage = HomepageDialog()
        self.homepage.setupUi(self.home_page_form)
        #Dialog.hide()
        self.home_page_form.show() 

    
    def open_profile_ui_form(self,event):
        from profile_ui import Ui_Dialog as SigninDialog
        self.profile_form = QtWidgets.QDialog()
        self.profile_ui = SigninDialog()
        self.profile_ui.setupUi(self.profile_form)
        self.profile_form.show()
        #self.Dialog.hide()    
    
    def open_profile_ui_form(self,event):
        from profile_ui import Ui_Dialog as SigninDialog
        self.profile_form = QtWidgets.QDialog()
        self.profile_ui = SigninDialog()
        self.profile_ui.setupUi(self.profile_form)
        self.profile_form.show()
    
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

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Pending Invitations"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Accept"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Ignore"))
        self.label_6.setText(_translate("Dialog", "                  Invitations"))
        self.label_7.setText(_translate("Dialog", "            Connect With People"))
        
import homelinkedin
import homepage
import messagepic
import networkpic
import profilepic

first_name_of_f = ""
last_name_of_f = ""
email_of_f = ""
password_of_f = 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
