# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'distance.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Distance(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.color_frame = QtWidgets.QLabel(self.centralwidget)
        self.color_frame.setGeometry(QtCore.QRect(260, 100, 640, 480))
        self.color_frame.setMinimumSize(QtCore.QSize(640, 480))
        self.color_frame.setMaximumSize(QtCore.QSize(640, 480))
        self.color_frame.setText("")
        self.color_frame.setObjectName("color_frame")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 250, 176, 130))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.point1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.point1.setObjectName("point1")
        self.horizontalLayout.addWidget(self.point1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.point2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.point2.setObjectName("point2")
        self.horizontalLayout_2.addWidget(self.point2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.get_frame = QtWidgets.QPushButton(self.layoutWidget)
        self.get_frame.setObjectName("get_frame")
        self.verticalLayout.addWidget(self.get_frame)
        self.start_measure = QtWidgets.QPushButton(self.layoutWidget)
        self.start_measure.setObjectName("start_measure")
        self.verticalLayout.addWidget(self.start_measure)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 23))
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
        self.label.setText(_translate("MainWindow", "point 1"))
        self.label_2.setText(_translate("MainWindow", "point 2"))
        self.get_frame.setText(_translate("MainWindow", "获取图片"))
        self.start_measure.setText(_translate("MainWindow", "开始测量"))

