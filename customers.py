import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Прописуєм логіку кнопки

class Customer:
    firstName = ''
    lastName = ''
    middleName = ''
    birthdayDate = ''
    phoneNumber = ''
    email = ''
    sex = ''

    def updateTxt():
        data = open("customers.txt","w")
        data.write(Customer.firstName+"\n")
        data.write(Customer.lastName+"\n")
        data.write(Customer.middleName+"\n")
        data.write(Customer.birthdayDate+"\n")
        data.write(Customer.phoneNumber+"\n")
        data.write(Customer.email+"\n")
        data.write(Customer.sex+"\n")
        data.close()
        pass

def Save():
    Customer.lastName = ui.lineEdit_3.text()
    Customer.firstName = ui.lineEdit_2.text()
    Customer.middleName = ui.lineEdit_4.text()
    Customer.birthdayDate = ui.lineEdit_5.text()
    Customer.phoneNumber = ui.lineEdit_6.text()
    Customer.email = ui.lineEdit_8.text()
    Customer.sex = ui.comboBox.currentText()    
    Customer.updateTxt()

data = open("customers.txt","r")
temp = data.read().splitlines()
for i in range(len(temp)):
    Customer.firstName = temp[i]
    ui.lineEdit_2.setText(temp[i])
    i+=1
    Customer.lastName = temp[i]
    ui.lineEdit_3.setText(temp[i])
    i+=1
    Customer.middleName = temp[i]
    ui.lineEdit_4.setText(temp[i])
    i+=1
    Customer.birthdayDate = temp[i]
    ui.lineEdit_5.setText(temp[i])
    i+=1
    Customer.phoneNumber = temp[i]
    ui.lineEdit_6.setText(temp[i])
    i+=1
    Customer.email = temp[i]
    ui.lineEdit_8.setText(temp[i])
    i+=1
    Customer.sex = temp[i]
    ui.comboBox.setCurrentText(temp[i])
    if not data.readline():
        break

data.close()

ui.pushButton_3.clicked.connect(Save)

# виходим з вікна
sys.exit(app.exec_())