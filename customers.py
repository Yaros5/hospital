import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
ui = Ui_MainWindow()

# Прописуєм логіку кнопки

class Customer:
    login
    password
    firstName
    lastName
    middleName
    birthdayDate
    phoneNumber
    email
    sex

    def updateTxt():
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
    Customer.updateTxt()

def changePass():
    #change password
    pass

data = open("customers.txt","r")
while True:
    Doctors.firstName.append(data.readline())
    Doctors.lastName.append(data.readline())
    Doctors.age.append(data.readline())
    Doctors.exp.append(data.readline())
    Doctors.speciality.append(data.readline())
    Doctors.hours.append(data.readline())
    Doctors.price.append(data.readline())
    Doctors.password.append(data.readline())
    Doctors.login.append(Doctors.firstName[-1] + Doctors.lastName[-1])
    if not data.readline():
        break
data.close()

ui.pushButton_3.clicked.connect(Save)
ui.pushButton_4.clicked.connect(changePass)

# виходим з вікна
#sys.exit(app.exec_())