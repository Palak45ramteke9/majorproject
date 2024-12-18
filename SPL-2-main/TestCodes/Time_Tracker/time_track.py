# -*- coding: utf-8 -*-
import math

# Form implementation generated from reading ui file 'time_track.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time

from PyQt5.QtCore import QTimer


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(696, 475)

        self.s_time = None
        self.e_time = None

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 120, 171, 71))
        self.pushButton.setObjectName("start")

        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(350, 120, 171, 71))
        self.pushButton2.setObjectName("end")

        self.start_time = QtWidgets.QLabel(Form)
        self.start_time.setGeometry(QtCore.QRect(110, 270, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(18)
        self.start_time.setFont(font)
        self.start_time.setStyleSheet("background-color: bisque;")
        self.start_time.setText("")
        self.start_time.setObjectName("start_time")
        self.end_time = QtWidgets.QLabel(Form)
        self.end_time.setGeometry(QtCore.QRect(270, 270, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(18)
        self.end_time.setFont(font)
        self.end_time.setStyleSheet("background-color: bisque;")
        self.end_time.setText("")
        self.end_time.setObjectName("end_time")
        self.elapsed_time = QtWidgets.QLabel(Form)
        self.elapsed_time.setGeometry(QtCore.QRect(430, 270, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(15)
        self.elapsed_time.setFont(font)
        self.elapsed_time.setStyleSheet("background-color: bisque;")
        self.elapsed_time.setText("")
        self.elapsed_time.setObjectName("elapsed_time")

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTimer)
        self.pushButton.clicked.connect(self.startTimer)
        self.pushButton2.clicked.connect(self.endTimer)
        self.initTime = time.time()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def showTimer(self):
        currentTime = time.time()
        tt = (math.floor(currentTime - self.initTime))

        mins, secs = divmod(tt, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        self.elapsed_time.setText(timeformat)

    def startTimer(self):

        currentTime = time.time()
        self.start_time.setText(time.ctime(currentTime).split(' ')[3])
        self.s_time = currentTime

        print(time.ctime(currentTime).split(' ')[3])

        self.timer.start(1000)
        self.pushButton.setEnabled(False)
        self.pushButton2.setEnabled(True)

    def endTimer(self):
        currentTime = time.time()
        self.end_time.setText(time.ctime(currentTime).split(' ')[3])
        self.e_time = currentTime

        t = self.e_time - self.s_time
        formatted_t = time.ctime(t)

        print(time.ctime(currentTime).split(' ')[3])
        print("Elapsed: ", formatted_t)

        self.timer.stop()
        self.pushButton.setEnabled(True)
        self.pushButton2.setEnabled(False)
        self.initTime = time.time()


    def btnPressed(self):
        currentTime = time.time()
        self.start_time.setText(time.ctime(currentTime).split(' ')[3])
        self.s_time = currentTime

        print(time.ctime(currentTime).split(' ')[3])

        self.timer.startTimer()

    def btnPressed2(self):

        self.timer.endTimer()

        currentTime = time.time()
        self.end_time.setText(time.ctime(currentTime).split(' ')[3])
        self.e_time = currentTime

        t = self.e_time - self.s_time
        formatted_t = time.ctime(t).split(' ')[3]

        print(time.ctime(currentTime).split(' ')[3])

        min = t // 60
        sec = ((t / 60) - (t // 60)) * 60

        cur_time = str(min) + ": " + str(round(sec, 3))

        self.elapsed_time.setText(cur_time)

        print("Elapsed: ", min, ": ", sec)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.pushButton2.setText(_translate("Form", "End"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
