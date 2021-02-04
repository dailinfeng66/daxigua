# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from handle_file import pre_handle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 151, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 150, 341, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 481, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 281, 51))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_2.clicked.connect(self.select_file)
        self.pushButton.clicked.connect(self.submit)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "合成大西瓜自定义"))
        # 禁止拉伸窗口大小
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.label.setText(_translate("MainWindow", "选择照片文件夹路径:"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "请选择文件夹"))
        self.label_2.setText(_translate("MainWindow", " "))
        self.label_3.setText(_translate("MainWindow", ""))

    # 选择文件夹
    def select_file(self):
        dir_choose = QFileDialog.getExistingDirectory()  # 起始路径
        if dir_choose == "":
            print("\n取消选择")
            return
        self.label_2.setText(dir_choose)
        # print("\n你选择的文件夹为:")
        # print(dir_choose)

    def submit(self):
        label = self.label_2.text().strip()
        if label == "" or label == None:
            self.label_3.setText("请选择文件夹!")
            return
        else:
            filepath = f"{self.label_2.text()}\\"
            self.label_3.setText("正在加载.....")
            try:
                pre_handle(filepath)
                self.label_3.setText("转换完成,请打开utool部署")
            except Exception as e:
                try:
                    if "系统找不到指定的路径" in e:
                        self.label_3.setText("请选择正确文件夹!")
                    else:
                        self.label_3.setText(str(e))
                except:
                    self.label_3.setText(str(e))