from PyQt5 import QtCore, QtGui, QtWidgets
from hashing_implementation_log_in import HashTable 
ht_insatnce = HashTable()

class Ui_Dialog(object):
    def setupUi(self, Dialog,received_email=None):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1049, 566)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-130, -100, 1351, 161))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 0, 81, 61))
        self.label.setStyleSheet("image: url(:/newPrefix/homelinkedin.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(360, 0, 71, 61))
        self.label_2.setStyleSheet("image: url(:/newPrefix/homepic.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(520, 0, 91, 61))
        self.label_3.setStyleSheet("image: url(:/newPrefix/networkpic.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(710, 0, 81, 61))
        self.label_4.setStyleSheet("image: url(:/newPrefix/messagepic.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(870, 0, 91, 61))
        self.label_5.setStyleSheet("image: url(:/newPrefix/profilepic.jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(310, 110, 571, 311))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(310, 370, 431, 51))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(740, 370, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 120);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(590, 110, 291, 261))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(240)
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(310, 110, 281, 261))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setRowCount(1000)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(240)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        found_node = ht_insatnce.user_for_searching(received_email)
        item.setText(found_node.first_name + " " + found_node.last_name if received_email else "Received")
        #self.pushButton.clicked.connect(self.send_message)
        from mainpage_ui import email
        combined_email = f"{received_email}_{email}"
        self.load_messages(combined_email,received_email)
        
        self.label_4.mousePressEvent = self.open_messaging_ui_form
        self.label_5.mousePressEvent = self.open_profile_ui_form
        self.label_2.mousePressEvent = self.home_page
        self.label_3.mousePressEvent = self.my_network_ui_form

        self.pushButton.clicked.connect(lambda: self.send_message(received_email))
    def send_message(self,received_email):
        from mainpage_ui import email
        message_text = self.textEdit.toPlainText()        
        if message_text:
            current_row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(0)
            item = QtWidgets.QTableWidgetItem(message_text)
            self.tableWidget.setItem(0, 0, item)
            self.textEdit.clear()
            
            combined_email = f"{email}_{received_email}"
            with open(f"{combined_email}.txt", 'a') as file:
                file.write(message_text + ',')
                
    def load_messages(self, combinedemail, received_email):
        from mainpage_ui import email
        
        combined_email = f"{email}_{received_email}"
        parts = combined_email.split('_')

        try:
            if len(parts) == 2:
                friend_email, mainpage_email = parts
                print("Parts",parts,"---------")
                print(combined_email,"-----------")
                print("Friend_email",friend_email,"recived",received_email,mainpage_email,email)
                if ((friend_email == received_email and mainpage_email == email)):
                    print("in if",combined_email)
                    with open(f"{combined_email}.txt", 'r') as file:
                        messages = file.read().split(',')

                    messages = messages[:-1]
                    messages.reverse()
                    row_count = len(messages)
                    self.tableWidget_2.setRowCount(row_count)

                    for i, message in enumerate(messages):
                        item = QtWidgets.QTableWidgetItem(message)
                        self.tableWidget_2.setItem(i, 0, item)
                elif(friend_email == email and mainpage_email == received_email):
                    combined_email = f"{received_email}_{email}"
                    print("combinedEmail:",combined_email,"in elif")
                    # Handle file not found exception by opening a default file
                    with open(f"{combined_email}.txt", 'r') as file:
                        messages = file.read().split(',')
                        messages = messages[:-1]
                        messages.reverse()
                        row_count = len(messages)
                        self.tableWidget_2.setRowCount(row_count)

                        for i, message in enumerate(messages):
                            item = QtWidgets.QTableWidgetItem(message)
                            self.tableWidget_2.setItem(i, 0, item)
    
    
        except FileNotFoundError:
            pass

                
            
    def open_messaging_ui_form(self,event):
        from messaging_ui import Ui_Dialog as msgDialog
        self.msg_form = QtWidgets.QDialog()
        self.messaging_ui = msgDialog()
        self.messaging_ui.setupUi(self.msg_form)
        self.msg_form.show()    
        
    def my_network_ui_form(self,event):
        from mynetwork_ui import Ui_Dialog as networkDialog
        self.networkform = QtWidgets.QDialog()
        self.mynetwork_ui = networkDialog()
        self.mynetwork_ui.setupUi(self.networkform)
        self.networkform.show()
        
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
        self.textEdit.setPlaceholderText(_translate("Dialog", " Type Here"))
        self.pushButton.setText(_translate("Dialog", "Send Message"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Sent"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Received"))


import homelinkedin
import homepic
import logo
import messagepic
import networkpic
import profilepic



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    #ui.load_messages(received_email)
    Dialog.show()
    sys.exit(app.exec_())
