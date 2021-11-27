from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from window import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)



def bp():
    label_1 = ui.lineEdit.text()

    label_2 = ui.lineEdit_2.text()
    label_3 = ui.lineEdit_3.text()






ui.pushButton.clicked.connect(bp)


MainWindow.show()
sys.exit(app.exec_())

