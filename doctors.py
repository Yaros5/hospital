import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
ui = Ui_MainWindow()

# Прописуєм логіку кнопки

class Doctors:
    login = []
    password = []
    firstName = []
    lastName = []
    age = []
    exp = []
    speciality = []
    hours = []
    price = []

def Search():
    searchText = ui.lineEdit.text()
    for item in login:
        if Doctors.firstName[item].find(searchText) != -1 or Doctors.lastName[item].find(searchText) != -1 or Doctors.speciality[item].find(searchText) != -1:
            #gets data from this doctor
            pass

data = open("doctors.txt","r")
while True:
    Doctors.firstName.append(data.readline())
    Doctors.lastName.append(data.readline())
    Doctors.age.append(data.readline())
    Doctors.exp.append(data.readline())
    Doctors.speciality.append(data.readline())
    Doctors.hours.append(data.readline())
    Doctors.price.append(data.readline())
    Doctors.password.append(data.readline())
    Doctors.login.append(Doctors.firstName[-1] + "_" + Doctors.lastName[-1])
    if not data.readline():
        break
data.close()

print(Doctors.login)

ui.pushButton_2.clicked.connect(Search())

# виходим з вікна
# sys.exit(app.exec_())