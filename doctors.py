doctors_dict = {'firstname' :  ['Brian','Lydia','Cili','Rut','Xenagoras','Mathieu','Scarlet','Widald','Dimas','Armann','Vanda','Barnabas','Kristian','Sarit','Jennifer','Ales','Elo','Vaughan','Nausikaa'],
                'lastname' :   ['Schneider','Jokumsen','Kipling','Langer','Chaves','Nanni','Neil','Serra','Bergman','Fujimoto','Chester','Budai','Trevis','Ridge','Kazlow','Ruff','Carson','Marinov','MacAslan'],
                'age' :        ['20 y/o','58 y/o','55 y/o','29 y/o','43 y/o','63 y/o','41 y/o','33 y/o','29 y/o','31 y/o','55 y/o','45 y/o','29 y/o','25 y/o','38 y/o','54 y/o','59 y/o','39 y/o','63 y/o'],
                'experience' : ['2 years','16 years','30 years','8 years','20 years','29 years','8 years','7 years','6 years','10 years','31 years','16 years','8 years','4 years','12 years','27 years','35 years','9 years','28 years'],
                'specialty' :  ['ENT-doctor','ENT-doctor','ENT-doctor','Proctologist','Surgeon','Surgeon','Ophthalmologist','Ophthalmologist','Physician','Physician','Urologist','Cardiologist','Cardiologist','Endocrinologist','Neurologist','Oncologist','Dentist','Dentist'],
                'hours' :      ['9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00','9.00 - 18.00'],
                'price' :      ['12$','20$','25$','18$','24$','30$','17$','15$','25$','30$','20$','24$','22$','15$','21$','26$','35$','20$','27$']}

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