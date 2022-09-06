# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.verticalLayout.addWidget(self.label_status)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.radioButton_auto = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_auto.setObjectName("radioButton_auto")
        self.verticalLayout_2.addWidget(self.radioButton_auto)
        self.radioButton_manu = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_manu.setChecked(True)
        self.radioButton_manu.setObjectName("radioButton_manu")
        self.verticalLayout_2.addWidget(self.radioButton_manu)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.checkBox_clipboard = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_clipboard.setChecked(True)
        self.checkBox_clipboard.setObjectName("checkBox_clipboard")
        self.verticalLayout_2.addWidget(self.checkBox_clipboard)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton_selectArea = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selectArea.setEnabled(True)
        self.pushButton_selectArea.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_selectArea.setObjectName("pushButton_selectArea")
        self.verticalLayout_2.addWidget(self.pushButton_selectArea)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.pushButton_scan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_scan.setEnabled(False)
        self.pushButton_scan.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_scan.setObjectName("pushButton_scan")
        self.verticalLayout_2.addWidget(self.pushButton_scan)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.textBrowser_result = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_result.setObjectName("textBrowser_result")
        self.horizontalLayout_2.addWidget(self.textBrowser_result)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_status.setText(_translate("MainWindow", "Press [Select new area] to begin"))
        self.label_2.setText(_translate("MainWindow", "Scanning mode:"))
        self.radioButton_auto.setText(_translate("MainWindow", "Automatic"))
        self.radioButton_manu.setText(_translate("MainWindow", "Manual"))
        self.checkBox_clipboard.setText(_translate("MainWindow", "Copy result\n"
"to clipboard"))
        self.pushButton_selectArea.setText(_translate("MainWindow", "Select\n"
" new area"))
        self.pushButton_scan.setText(_translate("MainWindow", "Scan"))
