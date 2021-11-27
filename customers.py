import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
ui = Ui_MainWindow()

# getting current login from logging in
currentLogin = "Oleg_Sadovskyy"

# Прописуєм логіку кнопки

class Customer:
    login = []
    password = []
    firstName = []
    lastName = []
    middleName = []
    birthdayDate = []
    phoneNumber = []
    email = []
    sex = []

    def updateTxt():
        data = open("customers.txt","w")
        for item in firstName:
            data.write(Customer.firstName[item])
            data.write(Customer.lastName[item])
            data.write(Customer.middleName[item])
            data.write(Customer.birthdayDate[item])
            data.write(Customer.phoneNumber[item])
            data.write(Customer.email[item])
            data.write(Customer.sex[item])
            data.write(Customer.password[item])
        data.close()
        pass

def Save():
    Customer.lastName[index] = ui.lineEdit_2.text()
    Customer.firstName[index] = ui.lineEdit_3.text()
    Customer.middleName[index] = ui.lineEdit_4.text()
    Customer.birthdayDate[index] = ui.lineEdit_5.text()
    Customer.phoneNumber[index] = ui.lineEdit_6.text()
    Customer.email[index] = ui.lineEdit_7.text()
    Customer.sex[index] = ui.comboBox.currentText()    
    Customer.updateTxt()

data = open("customers.txt","r")
temp = data.read().splitlines()
for i in range(len(temp)):
    Customer.firstName.append(temp[i])
    i+=1
    Customer.lastName.append(temp[i])
    i+=1
    Customer.middleName.append(temp[i])
    i+=1
    Customer.birthdayDate.append(temp[i])
    i+=1
    Customer.phoneNumber.append(temp[i])
    i+=1
    Customer.email.append(temp[i])
    i+=1
    Customer.sex.append(temp[i])
    i+=1
    Customer.password.append(temp[i])
    i+=1
    Customer.login.append(Customer.firstName[-1] + "_" + Customer.lastName[-1])
    if not data.readline():
        break
print(Customer.firstName)
index = Customer.login.index(currentLogin)
data.close()

ui.pushButton_3.clicked.connect(Save())

# виходим з вікна
#sys.exit(app.exec_())