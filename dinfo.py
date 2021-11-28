import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow
from doc1 import Ui_MainWindow_1
from doc2 import Ui_MainWindow_2
from doc3 import Ui_MainWindow_3
from doc4 import Ui_MainWindow_4
from doc5 import Ui_MainWindow_5
from doc6 import Ui_MainWindow_6
from doc7 import Ui_MainWindow_7
from doc8 import Ui_MainWindow_8
from doc9 import Ui_MainWindow_9
from doc10 import Ui_MainWindow_10
from doc11 import Ui_MainWindow_11
from doc12 import Ui_MainWindow_12
from doc13 import Ui_MainWindow_13
from doc14 import Ui_MainWindow_14
from doc15 import Ui_MainWindow_15
from doc16 import Ui_MainWindow_16
from doc17 import Ui_MainWindow_17
from doc18 import Ui_MainWindow_18
from doc19 import Ui_MainWindow_19
from appointment import Ui_MainWindow_B
#import customers

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

MainW1 = QtWidgets.QMainWindow()
ui1 = Ui_MainWindow_1()
ui1.setupUi(MainW1)

MainW2 = QtWidgets.QMainWindow()
ui2 = Ui_MainWindow_2()
ui2.setupUi(MainW2)

MainW3 = QtWidgets.QMainWindow()
ui3 = Ui_MainWindow_3()
ui3.setupUi(MainW3)

MainW4 = QtWidgets.QMainWindow()
ui4 = Ui_MainWindow_4()
ui4.setupUi(MainW4)

MainW5 = QtWidgets.QMainWindow()
ui5 = Ui_MainWindow_5()
ui5.setupUi(MainW5)

MainW6 = QtWidgets.QMainWindow()
ui6 = Ui_MainWindow_6()
ui6.setupUi(MainW6)

MainW7 = QtWidgets.QMainWindow()
ui7 = Ui_MainWindow_7()
ui7.setupUi(MainW7)

MainW8 = QtWidgets.QMainWindow()
ui8 = Ui_MainWindow_8()
ui8.setupUi(MainW8)

MainW9 = QtWidgets.QMainWindow()
ui9 = Ui_MainWindow_9()
ui9.setupUi(MainW9)

MainW10 = QtWidgets.QMainWindow()
ui10 = Ui_MainWindow_10()
ui10.setupUi(MainW10)

MainW11 = QtWidgets.QMainWindow()
ui11 = Ui_MainWindow_11()
ui11.setupUi(MainW11)

MainW12 = QtWidgets.QMainWindow()
ui12 = Ui_MainWindow_12()
ui12.setupUi(MainW12)

MainW13 = QtWidgets.QMainWindow()
ui13 = Ui_MainWindow_13()
ui13.setupUi(MainW13)

MainW14 = QtWidgets.QMainWindow()
ui14 = Ui_MainWindow_14()
ui14.setupUi(MainW14)

MainW15 = QtWidgets.QMainWindow()
ui15 = Ui_MainWindow_15()
ui15.setupUi(MainW15)

MainW16 = QtWidgets.QMainWindow()
ui16 = Ui_MainWindow_16()
ui16.setupUi(MainW16)

MainW17 = QtWidgets.QMainWindow()
ui17 = Ui_MainWindow_17()
ui17.setupUi(MainW17)

MainW18 = QtWidgets.QMainWindow()
ui18 = Ui_MainWindow_18()
ui18.setupUi(MainW18)

MainW19 = QtWidgets.QMainWindow()
ui19 = Ui_MainWindow_19()
ui19.setupUi(MainW19)

MainWBook = QtWidgets.QMainWindow()
uiB = Ui_MainWindow_B()
uiB.setupUi(MainWBook)


class Customer:
    firstName = ''
    lastName = ''
    middleName = ''
    birthdayDate = ''
    phoneNumber = ''
    email = ''
    sex = ''

    def updateTxt():
        data = open("customers.txt", "w")
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


def checkIfDefault():
    if ui.lineEdit_2.text() == "First name" or ui.lineEdit_3.text() == "Last name" or ui.lineEdit_4.text() == "Middle name" or ui.lineEdit_5.text() == "Date of birth" or ui.lineEdit_6.text() == "Phone number" or ui.lineEdit_8.text() == "Email":
        return 1
    else:
        return 0


def botBook():
    #id = 780892851
    if checkIfDefault() == 1:
        closeAll()
        return
    global date, time, fullName
    fullName = Customer.firstName + " \"" + \
        Customer.middleName + "\" " + Customer.lastName
    date = uiB.dateEdit.date().toString("dd.MM.yyyy")
    time = uiB.timeEdit.time().toString("hh:mm")
    closeAll()


def closeAll():
    MainWBook.close()
    close1()
    close2()
    close3()
    close4()
    close5()
    close6()
    close7()
    close8()
    close9()
    close10()
    close11()
    close12()
    close13()
    close14()
    close15()
    close16()
    close17()
    close18()
    close19()


def book():
    MainWBook.show()
    uiB.pushButton_2.clicked.connect(closeB)
    uiB.pushButton_1.clicked.connect(botBook)


def closeB():
    MainWBook.close()


def open1():
    MainW1.show()
    ui1.pushButton_1.clicked.connect(close1)
    ui1.pushButton_2.clicked.connect(book)


def close1():
    MainW1.close()


def open2():
    MainW2.show()
    ui2.pushButton_1.clicked.connect(close2)
    ui2.pushButton_2.clicked.connect(book)


def close2():
    MainW2.close()


def open3():
    MainW3.show()
    ui3.pushButton_1.clicked.connect(close3)
    ui3.pushButton_2.clicked.connect(book)


def close3():
    MainW3.close()


def open4():
    MainW4.show()
    ui4.pushButton_1.clicked.connect(close4)
    ui4.pushButton_2.clicked.connect(book)


def close4():
    MainW4.close()


def open5():
    MainW5.show()
    ui5.pushButton_1.clicked.connect(close5)
    ui5.pushButton_2.clicked.connect(book)


def close5():
    MainW5.close()


def open6():
    MainW6.show()
    ui6.pushButton_1.clicked.connect(close6)
    ui6.pushButton_2.clicked.connect(book)


def close6():
    MainW6.close()


def open7():
    MainW7.show()
    ui7.pushButton_1.clicked.connect(close7)
    ui7.pushButton_2.clicked.connect(book)


def close7():
    MainW7.close()


def open8():
    MainW8.show()
    ui8.pushButton_1.clicked.connect(close8)
    ui8.pushButton_2.clicked.connect(book)


def close8():
    MainW8.close()


def open9():
    MainW9.show()
    ui9.pushButton_1.clicked.connect(close9)
    ui9.pushButton_2.clicked.connect(book)


def close9():
    MainW9.close()


def open10():
    MainW10.show()
    ui10.pushButton_1.clicked.connect(close10)
    ui10.pushButton_2.clicked.connect(book)


def close10():
    MainW10.close()


def open11():
    MainW11.show()
    ui11.pushButton_1.clicked.connect(close11)
    ui11.pushButton_2.clicked.connect(book)


def close11():
    MainW11.close()


def open12():
    MainW12.show()
    ui12.pushButton_1.clicked.connect(close12)
    ui12.pushButton_2.clicked.connect(book)


def close12():
    MainW12.close()


def open13():
    MainW13.show()
    ui13.pushButton_1.clicked.connect(close13)
    ui13.pushButton_2.clicked.connect(book)


def close13():
    MainW13.close()


def open14():
    MainW14.show()
    ui14.pushButton_1.clicked.connect(close14)
    ui14.pushButton_2.clicked.connect(book)


def close14():
    MainW14.close()


def open15():
    MainW15.show()
    ui15.pushButton_1.clicked.connect(close15)
    ui15.pushButton_2.clicked.connect(book)


def close15():
    MainW15.close()


def open16():
    MainW16.show()
    ui16.pushButton_1.clicked.connect(close16)
    ui16.pushButton_2.clicked.connect(book)


def close16():
    MainW16.close()


def open17():
    MainW17.show()
    ui17.pushButton_1.clicked.connect(close17)
    ui17.pushButton_2.clicked.connect(book)


def close17():
    MainW17.close()


def open18():
    MainW18.show()
    ui18.pushButton_1.clicked.connect(close18)
    ui18.pushButton_2.clicked.connect(book)


def close18():
    MainW18.close()


def open19():
    MainW19.show()
    ui19.pushButton_1.clicked.connect(close19)
    ui19.pushButton_2.clicked.connect(book)


def close19():
    MainW19.close()


def binary_Search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


list_doctor = ['Ales Ruff', 'Armann Fujimoto', 'Barnabas Budai', 'Brian Schneider', 'Cili Kipling', 'Dimas Bergman',
               'Elo Carson', 'Jennifer Kazlow', 'Kristian Trevis', 'Lydia Jokumsen', 'Mathieu Nanni',
               'Nausikaa MacAslan',
               'Rut Langer', 'Sarit Ridge', 'Scarlet Neil', 'Vanda Chester', 'Vaughan Marinov', 'Widald Serra',
               'Xenagoras Chaves']
list_specification = ['ENT-doctor', 'Proctologist', 'Surgeon', 'Ophthalmologist', 'Physician',
                      'Urologist', 'Cardiologist', 'Endocrinologist', 'Neurologist',
                      'Oncologist', 'Dentist']

ui.pushButton_4.setStyleSheet("QPushButton {\n"
                              "  padding: 15px 30px;\n"
                              "  font-size: 16px;\n"
                              "  border-radius: 15px;\n"
                              "  background-color: #F9DFF9;\n"
                              "  border: none;\n"
                              "  color: #000;\n"

                              "}\n"
                              "\n"
                              "QPushButton:pressed {\n"
                              "  background: #f7f2f2;\n"
                              "}")
ui.pushButton_24.setStyleSheet("QPushButton {\n"
                               "  padding: 15px 30px;\n"
                               "  font-size: 16px;\n"
                               "  border-radius: 15px;\n"
                               "  background-color: #F9DFF9;\n"
                               "  border: none;\n"
                               "  color: #000;\n"

                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "  background: #f7f2f2;\n"
                               "}")
ui.pushButton_25.setStyleSheet("QPushButton {\n"
                               "  padding: 15px 30px;\n"
                               "  font-size: 16px;\n"
                               "  border-radius: 15px;\n"
                               "  background-color: #F9DFF9;\n"
                               "  border: none;\n"
                               "  color: #000;\n"

                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "  background: #f7f2f2;\n"
                               "}")


def search():
    a = ui.lineEdit_46.text()
    place = binary_Search(list_doctor, a)
    if a in list_doctor:
        ui.pushButton_4.setText(f'Doctor {a} ')
        ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                      "  padding: 15px 30px;\n"
                                      "  font-size: 16px;\n"
                                      "  border-radius: 15px;\n"
                                      "  background-color: #FFA;\n"
                                      "  border: none;\n"
                                      "  color: #000;\n"

                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "  background: #f7f2f2;\n"
                                      "}")
    if a in list_specification:
        if a == 'ENT-doctor':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")
            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #FAFAFA;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #FFA;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")

            ui.pushButton_4.setText('Brian Schneider')
            ui.pushButton_4.clicked.connect(open4)
            ui.pushButton_24.setText('Lydia Jokumsen')
            ui.pushButton_24.clicked.connect(open10)
            ui.pushButton_25.setText('Cili Kipling')
            ui.pushButton_25.clicked.connect(open5)

        if a == 'Proctologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")

            ui.pushButton_4.setText('Brian Schneider')
            ui.pushButton_24.setText('')
            ui.pushButton_25.setText('')
        if a == 'Surgeon':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")
            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FAFAFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")

            ui.pushButton_4.setText('Mathieu Nanni')
            ui.pushButton_24.setText('Xenagoras Chaves')
            ui.pushButton_25.setText('')
        if a == 'Ophthalmologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")
            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FAFAFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")

            ui.pushButton_4.setText('Scarlet Neil')
            ui.pushButton_24.setText('Widald Serra')
            ui.pushButton_25.setText('')

        if a == 'Physician':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FAFAFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")

            ui.pushButton_4.setText('Dimas Bergman')
            ui.pushButton_24.setText('Armann Fujimoto')
            ui.pushButton_25.setText('')
        if a == 'Urologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FAFAFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")

            ui.pushButton_4.setText('Vanda Chester')
            ui.pushButton_24.setText('Jennifer Kazlow')
            ui.pushButton_25.setText('')

        if a == 'Cardiologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FAFAFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")

            ui.pushButton_4.setText('Kristian Trevis')
            ui.pushButton_24.setText('Barnabas Budai')
            ui.pushButton_25.setText('')

        if a == 'Endocrinologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")

            ui.pushButton_4.setText('Sarit Ridge')
            ui.pushButton_24.setText('')
            ui.pushButton_25.setText('')

        if a == 'Neurologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")

            ui.pushButton_4.setText('Jennifer Kazlow')
            ui.pushButton_24.setText('')
            ui.pushButton_25.setText('')
        if a == 'Oncologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")

            ui.pushButton_4.setText('Elo Carson')
            ui.pushButton_24.setText('')
            ui.pushButton_25.setText('')
        if a == 'Dentist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FAFAFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #FFA;\n"
                                        "}")

            ui.pushButton_4.setText('Vaughan Marinov')
            ui.pushButton_24.setText('Nausikaa MacAslan')
            ui.pushButton_25.setText('')

        else:
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #FFA;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #f7f2f2;\n"
                                        "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                        "  padding: 15px 30px;\n"
                                        "  font-size: 16px;\n"
                                        "  border-radius: 15px;\n"
                                        "  background-color: #F9DFF9;\n"
                                        "  border: none;\n"
                                        "  color: #000;\n"

                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "  background: #F9DFF9;\n"
                                        "}")

            ui.pushButton_4.setText('Нічого не знайдено')

# Функція пошуку


data = open("customers.txt", "r")
temp = data.read().splitlines()
for i in range(len(temp)):
    Customer.firstName = temp[i]
    ui.lineEdit_2.setText(temp[i])
    i += 1
    Customer.lastName = temp[i]
    ui.lineEdit_3.setText(temp[i])
    i += 1
    Customer.middleName = temp[i]
    ui.lineEdit_4.setText(temp[i])
    i += 1
    Customer.birthdayDate = temp[i]
    ui.lineEdit_5.setText(temp[i])
    i += 1
    Customer.phoneNumber = temp[i]
    ui.lineEdit_6.setText(temp[i])
    i += 1
    Customer.email = temp[i]
    ui.lineEdit_8.setText(temp[i])
    i += 1
    Customer.sex = temp[i]
    ui.comboBox.setCurrentText(temp[i])
    if not data.readline():
        break

data.close()

ui.pushButton_3.clicked.connect(Save)

ui.pushButton_26.clicked.connect(search)

ui.pushButton_5.clicked.connect(open1)
ui.pushButton_6.clicked.connect(open2)
ui.pushButton_7.clicked.connect(open3)
ui.pushButton_8.clicked.connect(open4)
ui.pushButton_9.clicked.connect(open5)
ui.pushButton_10.clicked.connect(open6)
ui.pushButton_11.clicked.connect(open7)
ui.pushButton_12.clicked.connect(open8)
ui.pushButton_13.clicked.connect(open9)
ui.pushButton_14.clicked.connect(open10)
ui.pushButton_15.clicked.connect(open11)
ui.pushButton_16.clicked.connect(open12)
ui.pushButton_17.clicked.connect(open13)
ui.pushButton_18.clicked.connect(open14)
ui.pushButton_19.clicked.connect(open15)
ui.pushButton_20.clicked.connect(open16)
ui.pushButton_21.clicked.connect(open17)
ui.pushButton_22.clicked.connect(open18)
ui.pushButton_23.clicked.connect(open19)

# виходим з вікна
sys.exit(app.exec_())
