# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        MainWindow.setMaximumSize(QtCore.QSize(1400, 800))
        MainWindow.setStyleSheet("background-color: #F9DFF9;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1400, 800))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1400, 800))
        self.tabWidget.setWhatsThis("")
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setAccessibleDescription("")
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("background-color: #F9DFF9;")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(480, 120, 470, 80))
        self.label.setStyleSheet("font-size: 40px;\n"
"color: #222222;\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(440, 200, 520, 35))
        self.label_2.setStyleSheet("font-size: 25px;\n"
"color: #3E3E3E;\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(270, 310, 866, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
"  padding: 15px 30px;\n"
"  font-size: 16px;\n"
"  border-radius: 15px;\n"
"  background: #FAFAFA;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #f7f2f2;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setToolTip("")
        self.lineEdit.setStatusTip("")
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setAccessibleName("")
        self.lineEdit.setAccessibleDescription("")
        self.lineEdit.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"  padding: 15px 30px;\n"
"  font-size: 16px;\n"
"  border-radius: 15px;\n"
"  background: #2780DD;\n"
"  border: none;\n"
"  text-align: center;\n"
"  color: #fff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #2B5DAA;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(522, 390, 469, 49))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"  padding: 15px 30px;\n"
"  font-size: 16px;\n"
"  border-radius: 15px;\n"
"  background: #FAFAFA;\n"
"  border: none;\n"
"  color: #fff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #f7f2f2;\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1374, 747))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 1, 3, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 3, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 2, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setStyleSheet("")
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setStyleSheet("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 3, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 3, 3, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 255, 255))
        self.label_3.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(360, 120, 971, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(392, 110, 101, 17))
        self.label_4.setStyleSheet("color:#7f8c8d")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(731, 110, 91, 17))
        self.label_5.setStyleSheet("color:#7f8c8d")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(1071, 110, 111, 17))
        self.label_6.setStyleSheet("color:#7f8c8d")
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(700, 250, 290, 51))
        self.lineEdit_5.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(730, 223, 171, 17))
        self.label_8.setStyleSheet("color:#7f8c8d")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(565, 380, 270, 35))
        self.label_9.setStyleSheet("font-size: 25px;\n"
"color: #3E3E3E;\n"
"\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(565, 25, 270, 35))
        self.label_10.setStyleSheet("font-size: 25px;\n"
"color: #3E3E3E;\n"
"\n"
"")
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(230, 450, 971, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(250)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_6.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_8.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(262, 440, 181, 17))
        self.label_11.setStyleSheet("color:#7f8c8d")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(872, 440, 211, 17))
        self.label_12.setStyleSheet("color:#7f8c8d")
        self.label_12.setObjectName("label_12")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(625, 620, 150, 49))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"  padding: 15px 30px;\n"
"  font-size: 16px;\n"
"  border-radius: 15px;\n"
"  background: #2780DD;\n"
"  border: none;\n"
"  text-align: center;\n"
"  color: #fff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #2B5DAA;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(360, 250, 290, 51))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"color: #000")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(392, 223, 171, 17))
        self.label_13.setStyleSheet("color:#7f8c8d")
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Шукайте лікарів онлайн"))
        self.label_2.setText(_translate("MainWindow", "Записуйтесь на прийом не виходячи з дому"))
        self.pushButton.setText(_translate("MainWindow", "Записатись до лікаря"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введіть прізвище або спеціальність"))
        self.pushButton_2.setText(_translate("MainWindow", "Знайти"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main Page"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Doctors"))
        self.lineEdit_2.setText(_translate("MainWindow", "Прізвище"))
        self.lineEdit_3.setText(_translate("MainWindow", "Ім\'я"))
        self.lineEdit_4.setText(_translate("MainWindow", "По батькові"))
        self.label_4.setText(_translate("MainWindow", "Прізвище*"))
        self.label_5.setText(_translate("MainWindow", "Ім\'я*"))
        self.label_6.setText(_translate("MainWindow", "По батькові*"))
        self.lineEdit_5.setText(_translate("MainWindow", "Дата народження"))
        self.label_8.setText(_translate("MainWindow", "Дата народження*"))
        self.label_9.setText(_translate("MainWindow", "Контактна інформація"))
        self.label_10.setText(_translate("MainWindow", "Особиста інформація"))
        self.lineEdit_6.setText(_translate("MainWindow", "Номер телефону"))
        self.lineEdit_8.setText(_translate("MainWindow", "Електронна адреса"))
        self.label_11.setText(_translate("MainWindow", "Номер телефону*"))
        self.label_12.setText(_translate("MainWindow", "Електронна адреса*"))
        self.pushButton_3.setText(_translate("MainWindow", "Зберегти"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Чоловіча"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Жіноча"))
        self.label_13.setText(_translate("MainWindow", "Стать*"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "My Profile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
