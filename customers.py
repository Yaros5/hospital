import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
ui = Ui_MainWindow()

# Прописуєм логіку кнопки

class Customer:
    #getting data from logging in
    login
    password
    #getting data from database
    firstName
    lastName
    middleName
    birthdayDate
    phoneNumber
    email
    sex

    def updateDb():
        #updating database
        pass

def Save():
    Customer.lastname = ui.lineEdit_2.text()
    Customer.firstname = ui.lineEdit_3.text()
    Customer.middlename = ui.lineEdit_4.text()
    Customer.birthdayDate = ui.lineEdit_5.text()
    Customer.phoneNumber = ui.lineEdit_6.text()
    Customer.email = ui.lineEdit_7.text()
    Customer.sex = ui.comboBox.text()    
    Customer.updateDb()

def changePass():
    #change pass
    pass

ui.pushButton_3.clicked.connect(Save)
ui.pushButton_4.clicked.connect(changePass)

# виходим з вікна
#sys.exit(app.exec_())