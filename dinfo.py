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

def open1():
    MainW1.show()

def open2():
    MainW2.show()

def open3():
    MainW3.show()

def open4():
    MainW4.show()

def open5():
    MainW5.show()

def open6():
    MainW6.show()

def open7():
    MainW7.show()

def open8():
    MainW8.show()

def open9():
    MainW9.show()

def open10():
    MainW10.show()

def open11():
    MainW11.show()

def open12():
    MainW12.show()

def open13():
    MainW13.show()

def open14():
    MainW14.show()

def open15():
    MainW15.show()

def open16():
    MainW16.show()

def open17():
    MainW17.show()

def open18():
    MainW18.show()

def open19():
    MainW19.show()

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