import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
ui = Ui_MainWindow()

# Прописуєм логіку кнопки

class Doctors:
    #getting data from database
    login = {}
    password = {}
    firstName = {}
    lastName = {}
    age = {}
    exp = {}
    speciality = {}
    hours = {}
    price = {}

def Search():
    searchText = ui.lineEdit.text()
    for item in login:
        if Doctors.firstName[item].find(searchText) != -1 or Doctors.lastName[item].find(searchText) != -1 or Doctors.speciality[item].find(searchText) != -1:
            #gets data from this doctor
            pass
        
ui.pushButton_2.clicked.connect(Search())

# виходим з вікна
#sys.exit(app.exec_())