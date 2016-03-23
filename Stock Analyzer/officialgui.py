# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinalDraft.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#from ProClass import Stock
from ProClass import *

import urllib
import smtplib
import numpy
import getpass
import os
import pandas
import pyqtgraph as pg
import tkMessageBox, Tkinter

#read tickers into dictionary

tFile = pandas.read_csv("tickers.csv")

symbols = tFile['Symbol']
names = tFile['Name']



#make dictionary and fill
#
fileTest = os.path.exists("C:\\Users\\" + str(getpass.getuser())+ "\\AppData\\Local\\StockAnalyzer\\portfolio.txt")

theTickers = []
print theTickers

if fileTest == True:
    #read tickers from file into array
    content = file.readlines()
   
    for line in content:
        theTickers.append()

    report_types = [] #enter report types here
   
    for x in len(theTickers):
        for y in len(report_types):
            url = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=" + theTickers[x] + "&reportType=" + report_types[y] + "&period=12&dataType=A&order=asc&columnYear=5&number=3"


###### MAIN GUI STARTS BELOW #######
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(699, 727)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Investments = QtGui.QWidget()
        self.Investments.setObjectName(_fromUtf8("Investments"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Investments)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.Investments)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2.addWidget(self.groupBox_2, 3, 3, 2, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.Investments)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.matplotlibwidget_6 = MatplotlibWidget(self.groupBox_3)
        self.matplotlibwidget_6.setGeometry(QtCore.QRect(10, 20, 471, 131))
        self.matplotlibwidget_6.setObjectName(_fromUtf8("matplotlibwidget_6"))
        self.gridLayout_2.addWidget(self.groupBox_3, 4, 0, 1, 3)
        self.pushButton_2 = QtGui.QPushButton(self.Investments)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 5, 2, 1, 2)
        self.label = QtGui.QLabel(self.Investments)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 4)
        self.radioButton_3 = QtGui.QRadioButton(self.Investments)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.gridLayout_2.addWidget(self.radioButton_3, 1, 0, 1, 1)
        self.radioButton_4 = QtGui.QRadioButton(self.Investments)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.gridLayout_2.addWidget(self.radioButton_4, 1, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.Investments)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.Investments)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 2, 1, 1, 3)
        self.frame = QtGui.QFrame(self.Investments)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton_6 = QtGui.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 0, 151, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(170, 0, 151, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.frame, 5, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(self.Investments)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_stockprice = QtGui.QLabel(self.groupBox)
        self.label_stockprice.setGeometry(QtCore.QRect(10, 20, 160, 21))
        self.label_stockprice.setObjectName(_fromUtf8("label_stockprice"))
        self.label_roi = QtGui.QLabel(self.groupBox)
        self.label_roi.setGeometry(QtCore.QRect(10, 41, 160, 21))
        self.label_roi.setObjectName(_fromUtf8("label_roi"))
        self.label_debtequity = QtGui.QLabel(self.groupBox)
        self.label_debtequity.setGeometry(QtCore.QRect(10, 60, 160, 31))
        self.label_debtequity.setObjectName(_fromUtf8("label_debtequity"))
        self.label_netprofitmargin = QtGui.QLabel(self.groupBox)
        self.label_netprofitmargin.setGeometry(QtCore.QRect(10, 90, 160, 21))
        self.label_netprofitmargin.setObjectName(_fromUtf8("label_netprofitmargin"))
        self.label_revenue = QtGui.QLabel(self.groupBox)
        self.label_revenue.setGeometry(QtCore.QRect(10, 110, 160, 31))
        self.label_revenue.setObjectName(_fromUtf8("label_revenue"))
        self.label_recommendation = QtGui.QLabel(self.groupBox)
        self.label_recommendation.setGeometry(QtCore.QRect(10, 130, 160, 41))
        self.label_recommendation.setObjectName(_fromUtf8("label_recommendation"))
        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 3)
        self.tabWidget.addTab(self.Investments, _fromUtf8(""))
        self.Portfolio = QtGui.QWidget()
        self.Portfolio.setObjectName(_fromUtf8("Portfolio"))
        self.gridLayout_5 = QtGui.QGridLayout(self.Portfolio)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_3 = QtGui.QLabel(self.Portfolio)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 2)
        self.groupBox_5 = QtGui.QGroupBox(self.Portfolio)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.listWidget = QtGui.QListWidget(self.groupBox_5)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_3.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.Portfolio)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_5.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.Portfolio)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.listWidget_2 = QtGui.QListWidget(self.groupBox_6)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.gridLayout_4.addWidget(self.listWidget_2, 0, 0, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.groupBox_6)
        self.dateEdit.setDate(QtCore.QDate(2015, 12, 25))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout_4.addWidget(self.dateEdit, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_6, 2, 0, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(self.Portfolio)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.gridLayout_5.addWidget(self.groupBox_7, 2, 1, 1, 1)
        self.tabWidget.addTab(self.Portfolio, _fromUtf8(""))
        self.Details = QtGui.QWidget()
        self.Details.setObjectName(_fromUtf8("Details"))
        self.gridLayout_11 = QtGui.QGridLayout(self.Details)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.toolBox = QtGui.QToolBox(self.Details)
        self.toolBox.setEnabled(True)
        self.toolBox.setAcceptDrops(False)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.Stock1 = QtGui.QWidget()
        self.Stock1.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.Stock1.setObjectName(_fromUtf8("Stock1"))
        self.groupBox_16 = QtGui.QGroupBox(self.Stock1)
        self.groupBox_16.setGeometry(QtCore.QRect(0, 0, 407, 190))
        self.groupBox_16.setObjectName(_fromUtf8("groupBox_16"))
        self.gridLayout_10 = QtGui.QGridLayout(self.groupBox_16)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.groupBox_17 = QtGui.QGroupBox(self.groupBox_16)
        self.groupBox_17.setObjectName(_fromUtf8("groupBox_17"))
        self.gridLayout_10.addWidget(self.groupBox_17, 0, 0, 5, 1)
        self.checkBox_22 = QtGui.QCheckBox(self.groupBox_16)
        self.checkBox_22.setObjectName(_fromUtf8("checkBox_22"))
        self.gridLayout_10.addWidget(self.checkBox_22, 0, 1, 1, 2)
        self.checkBox_23 = QtGui.QCheckBox(self.groupBox_16)
        self.checkBox_23.setObjectName(_fromUtf8("checkBox_23"))
        self.gridLayout_10.addWidget(self.checkBox_23, 1, 1, 1, 2)
        self.checkBox_24 = QtGui.QCheckBox(self.groupBox_16)
        self.checkBox_24.setObjectName(_fromUtf8("checkBox_24"))
        self.gridLayout_10.addWidget(self.checkBox_24, 2, 1, 1, 2)
        self.dateEdit_6 = QtGui.QDateEdit(self.groupBox_16)
        self.dateEdit_6.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 12, 10), QtCore.QTime(0, 0, 0)))
        self.dateEdit_6.setObjectName(_fromUtf8("dateEdit_6"))
        self.gridLayout_10.addWidget(self.dateEdit_6, 3, 1, 1, 2)
        self.matplotlibwidget_5 = MatplotlibWidget(self.groupBox_16)
        self.matplotlibwidget_5.setObjectName(_fromUtf8("matplotlibwidget_5"))
        self.gridLayout_10.addWidget(self.matplotlibwidget_5, 4, 1, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.groupBox_16)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout_10.addWidget(self.pushButton_11, 4, 2, 1, 1)
        self.toolBox.addItem(self.Stock1, _fromUtf8(""))
        self.Stock2 = QtGui.QWidget()
        self.Stock2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.Stock2.setObjectName(_fromUtf8("Stock2"))
        self.groupBox_14 = QtGui.QGroupBox(self.Stock2)
        self.groupBox_14.setGeometry(QtCore.QRect(0, 0, 407, 190))
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_14)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.groupBox_15 = QtGui.QGroupBox(self.groupBox_14)
        self.groupBox_15.setObjectName(_fromUtf8("groupBox_15"))
        self.gridLayout_9.addWidget(self.groupBox_15, 0, 0, 5, 1)
        self.checkBox_19 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_19.setObjectName(_fromUtf8("checkBox_19"))
        self.gridLayout_9.addWidget(self.checkBox_19, 0, 1, 1, 2)
        self.checkBox_20 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_20.setObjectName(_fromUtf8("checkBox_20"))
        self.gridLayout_9.addWidget(self.checkBox_20, 1, 1, 1, 2)
        self.checkBox_21 = QtGui.QCheckBox(self.groupBox_14)
        self.checkBox_21.setObjectName(_fromUtf8("checkBox_21"))
        self.gridLayout_9.addWidget(self.checkBox_21, 2, 1, 1, 2)
        self.dateEdit_5 = QtGui.QDateEdit(self.groupBox_14)
        self.dateEdit_5.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 12, 10), QtCore.QTime(0, 0, 0)))
        self.dateEdit_5.setObjectName(_fromUtf8("dateEdit_5"))
        self.gridLayout_9.addWidget(self.dateEdit_5, 3, 1, 1, 2)
        self.matplotlibwidget_4 = MatplotlibWidget(self.groupBox_14)
        self.matplotlibwidget_4.setObjectName(_fromUtf8("matplotlibwidget_4"))
        self.gridLayout_9.addWidget(self.matplotlibwidget_4, 4, 1, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.groupBox_14)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout_9.addWidget(self.pushButton_10, 4, 2, 1, 1)
        self.toolBox.addItem(self.Stock2, _fromUtf8(""))
        self.Stock3 = QtGui.QWidget()
        self.Stock3.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.Stock3.setObjectName(_fromUtf8("Stock3"))
        self.groupBox_12 = QtGui.QGroupBox(self.Stock3)
        self.groupBox_12.setGeometry(QtCore.QRect(0, 0, 407, 190))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_12)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.groupBox_13 = QtGui.QGroupBox(self.groupBox_12)
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.gridLayout_8.addWidget(self.groupBox_13, 0, 0, 5, 1)
        self.checkBox_16 = QtGui.QCheckBox(self.groupBox_12)
        self.checkBox_16.setObjectName(_fromUtf8("checkBox_16"))
        self.gridLayout_8.addWidget(self.checkBox_16, 0, 1, 1, 2)
        self.checkBox_17 = QtGui.QCheckBox(self.groupBox_12)
        self.checkBox_17.setObjectName(_fromUtf8("checkBox_17"))
        self.gridLayout_8.addWidget(self.checkBox_17, 1, 1, 1, 2)
        self.checkBox_18 = QtGui.QCheckBox(self.groupBox_12)
        self.checkBox_18.setObjectName(_fromUtf8("checkBox_18"))
        self.gridLayout_8.addWidget(self.checkBox_18, 2, 1, 1, 2)
        self.dateEdit_4 = QtGui.QDateEdit(self.groupBox_12)
        self.dateEdit_4.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 12, 10), QtCore.QTime(0, 0, 0)))
        self.dateEdit_4.setObjectName(_fromUtf8("dateEdit_4"))
        self.gridLayout_8.addWidget(self.dateEdit_4, 3, 1, 1, 2)
        self.matplotlibwidget_3 = MatplotlibWidget(self.groupBox_12)
        self.matplotlibwidget_3.setObjectName(_fromUtf8("matplotlibwidget_3"))
        self.gridLayout_8.addWidget(self.matplotlibwidget_3, 4, 1, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_12)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout_8.addWidget(self.pushButton_9, 4, 2, 1, 1)
        self.toolBox.addItem(self.Stock3, _fromUtf8(""))
        self.Stock4 = QtGui.QWidget()
        self.Stock4.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.Stock4.setObjectName(_fromUtf8("Stock4"))
        self.groupBox_10 = QtGui.QGroupBox(self.Stock4)
        self.groupBox_10.setGeometry(QtCore.QRect(0, 0, 407, 190))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.groupBox_11 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.gridLayout_7.addWidget(self.groupBox_11, 0, 0, 5, 1)
        self.checkBox_13 = QtGui.QCheckBox(self.groupBox_10)
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.gridLayout_7.addWidget(self.checkBox_13, 0, 1, 1, 2)
        self.checkBox_14 = QtGui.QCheckBox(self.groupBox_10)
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.gridLayout_7.addWidget(self.checkBox_14, 1, 1, 1, 2)
        self.checkBox_15 = QtGui.QCheckBox(self.groupBox_10)
        self.checkBox_15.setObjectName(_fromUtf8("checkBox_15"))
        self.gridLayout_7.addWidget(self.checkBox_15, 2, 1, 1, 2)
        self.dateEdit_3 = QtGui.QDateEdit(self.groupBox_10)
        self.dateEdit_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 12, 10), QtCore.QTime(0, 0, 0)))
        self.dateEdit_3.setObjectName(_fromUtf8("dateEdit_3"))
        self.gridLayout_7.addWidget(self.dateEdit_3, 3, 1, 1, 2)
        self.matplotlibwidget_2 = MatplotlibWidget(self.groupBox_10)
        self.matplotlibwidget_2.setObjectName(_fromUtf8("matplotlibwidget_2"))
        self.gridLayout_7.addWidget(self.matplotlibwidget_2, 4, 1, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout_7.addWidget(self.pushButton_8, 4, 2, 1, 1)
        self.toolBox.addItem(self.Stock4, _fromUtf8(""))
        self.Stock5 = QtGui.QWidget()
        self.Stock5.setGeometry(QtCore.QRect(0, 0, 341, 169))
        self.Stock5.setObjectName(_fromUtf8("Stock5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.Stock5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_8 = QtGui.QGroupBox(self.Stock5)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_6.addWidget(self.groupBox_9, 0, 0, 5, 1)
        self.checkBox_12 = QtGui.QCheckBox(self.groupBox_8)
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.gridLayout_6.addWidget(self.checkBox_12, 0, 1, 1, 2)
        self.checkBox_11 = QtGui.QCheckBox(self.groupBox_8)
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.gridLayout_6.addWidget(self.checkBox_11, 1, 1, 1, 2)
        self.checkBox_10 = QtGui.QCheckBox(self.groupBox_8)
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.gridLayout_6.addWidget(self.checkBox_10, 2, 1, 1, 2)
        self.dateEdit_2 = QtGui.QDateEdit(self.groupBox_8)
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 12, 10), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.gridLayout_6.addWidget(self.dateEdit_2, 3, 1, 1, 2)
        self.matplotlibwidget = MatplotlibWidget(self.groupBox_8)
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))
        self.gridLayout_6.addWidget(self.matplotlibwidget, 4, 1, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_8)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout_6.addWidget(self.pushButton_7, 4, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_8)
        self.toolBox.addItem(self.Stock5, _fromUtf8(""))
        self.gridLayout_11.addWidget(self.toolBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Details, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "General Info", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Stock Performance (Graph)", None))
        self.pushButton_2.setText(_translate("MainWindow", "Add to Portfolio", None))
        self.label.setText(_translate("MainWindow", "BURMESE STOCK ANALYZER", None))
        self.radioButton_3.setText(_translate("MainWindow", "Search by Ticker", None))
        self.radioButton_4.setText(_translate("MainWindow", "Search by Company Name", None))
        self.label_2.setText(_translate("MainWindow", "Search ", None))
        self.lineEdit.setText(_translate("MainWindow", "Ex: Apple Inc", None))
        self.pushButton_6.setText(_translate("MainWindow", "Show Graph", None))
        self.pushButton.setText(_translate("MainWindow", "See Projection", None))
        self.groupBox.setTitle(_translate("MainWindow", "Stock Performance", None))
        self.label_stockprice.setText(_translate("MainWindow", "Stock Price", None))
        self.label_roi.setText(_translate("MainWindow", "ROI", None))
        self.label_debtequity.setText(_translate("MainWindow", "Debt to Equity", None))
        self.label_netprofitmargin.setText(_translate("MainWindow", "Net Profit Margin", None))
        self.label_revenue.setText(_translate("MainWindow", "Revenue", None))
        self.label_recommendation.setText(_translate("MainWindow", "Recommendation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Investments), _translate("MainWindow", "Investments", None))
        self.label_3.setText(_translate("MainWindow", "BURMESE STOCK (WHATEVER NAME IS HERE!)", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Portfolio", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Stock Performance (Graph)", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Select Time Frame", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Actions", None))
        self.pushButton_3.setText(_translate("MainWindow", "Buy", None))
        self.pushButton_4.setText(_translate("MainWindow", "Hold", None))
        self.pushButton_5.setText(_translate("MainWindow", "Sell", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Portfolio), _translate("MainWindow", "Portfolio", None))
        self.groupBox_16.setTitle(_translate("MainWindow", "Time Frame", None))
        self.groupBox_17.setTitle(_translate("MainWindow", "Stock Performance (Graph)", None))
        self.checkBox_22.setText(_translate("MainWindow", "Enter Date (Choose Date)", None))
        self.checkBox_23.setText(_translate("MainWindow", "Last Month", None))
        self.checkBox_24.setText(_translate("MainWindow", "Last Week", None))
        self.pushButton_11.setText(_translate("MainWindow", "Show Calendar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Stock1), _translate("MainWindow", "Stock1", None))
        self.groupBox_14.setTitle(_translate("MainWindow", "Time Frame", None))
        self.groupBox_15.setTitle(_translate("MainWindow", "Stock Performance (Graph)", None))
        self.checkBox_19.setText(_translate("MainWindow", "Enter Date (Choose Date)", None))
        self.checkBox_20.setText(_translate("MainWindow", "Last Month", None))
        self.checkBox_21.setText(_translate("MainWindow", "Last Week", None))
        self.pushButton_10.setText(_translate("MainWindow", "Show Calendar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Stock2), _translate("MainWindow", "Stock2", None))
        self.groupBox_12.setTitle(_translate("MainWindow", "Time Frame", None))
        self.groupBox_13.setTitle(_translate("MainWindow", "Stock Performance (Graph)", None))
        self.checkBox_16.setText(_translate("MainWindow", "Enter Date (Choose Date)", None))
        self.checkBox_17.setText(_translate("MainWindow", "Last Month", None))
        self.checkBox_18.setText(_translate("MainWindow", "Last Week", None))
        self.pushButton_9.setText(_translate("MainWindow", "Show Calendar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Stock3), _translate("MainWindow", "Stock3", None))
        self.groupBox_10.setTitle(_translate("MainWindow", "Time Frame", None))
        self.groupBox_11.setTitle(_translate("MainWindow", "Stock Performance (Graph)", None))
        self.checkBox_13.setText(_translate("MainWindow", "Enter Date (Choose Date)", None))
        self.checkBox_14.setText(_translate("MainWindow", "Last Month", None))
        self.checkBox_15.setText(_translate("MainWindow", "Last Week", None))
        self.pushButton_8.setText(_translate("MainWindow", "Show Calendar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Stock4), _translate("MainWindow", "Stock4", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "Time Frame", None))
        self.groupBox_9.setTitle(_translate("MainWindow", "Stock Performance (Graph)", None))
        self.checkBox_12.setText(_translate("MainWindow", "Enter Date (Choose Date)", None))
        self.checkBox_11.setText(_translate("MainWindow", "Last Month", None))
        self.checkBox_10.setText(_translate("MainWindow", "Last Week", None))
        self.pushButton_7.setText(_translate("MainWindow", "Show Calendar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Stock5), _translate("MainWindow", "Stock5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Details), _translate("MainWindow", "Details", None))
        self.pushButton_2.clicked.connect(self.addButton) #ADD
        self.pushButton.clicked.connect(self.seeProjection) #ADD
        self.pushButton_6.clicked.connect(self.ShowGraph) #CONNECTS WITH SHOW GRAPH FUNCTION

##########################ADD BELOW CODE TO NEW FILE####################################
    def addButton(self):
        t = str(self.lineEdit.text())
        if self.radioButton_3.isChecked():
            if t not in symbols:
                print "Ticker not found, moron please try again"
                errorString = "Stock Not Found, Please try again."
               
            elif t not in theTickers:
                    theTickers.append(t)
        if self.radioButton_4.isChecked():
            for i in names:
                if t in names:
                    theTickers.append(symbols[i])
       
        print theTickers

    def seeProjection(self):
       
        if self.radioButton_4.isChecked():
            print "YAY"
            co_name = str(self.lineEdit.text())
           
            new_ticker_file = open("tickers.csv")
            file_data_tickers = new_ticker_file.read().splitlines()
            new_ticker_file.close()
            for i in file_data_tickers:
                #print i
                col = i.split(",")
                a = col[0].upper()
                b = col[1].upper()
                nco_name = co_name.upper()
                b1 = b.split(" ")
                for i in range(len(b1)):
                    print b1[i]
                    if str(b1[i]) == str(nco_name):
                       print "!!!"
                       ticker = a
                       #st = Create_Stock_Info(ticker)
                #if b.find(nco_name) != -1:
                if nco_name in b:
                    print "!!!"
                    ticker = a
                    st = Create_Stock_Info(ticker)
                    #break
        else:
            ticker = str(self.lineEdit.text())
            #del stock_data[0]"""
        st = Create_Stock_Info(ticker)   
        #After the ticker is selected, this returns analyzed data
        portfolio = []
        #ticker = "FB"
        st = Create_Stock_Info(ticker)
        buffet_agrees = Buffett_Analyzer(ticker, st)
        print "Buffet_agrees Count is %s" % buffet_agrees

        #Possible values of "recommend" variable:
        #buy stok == 3
        #hold == 2
        #sell == 1

        if buffet_agrees >= 3.5:
            st.recommend = "Buy!"
        elif buffet_agrees < 3.5 and buffet_agrees >= 2:
            st.recommend = "Hold."
        else:
            st.recommend = "Stay Away!!!"
   
        #add stock to portfolio   
        portfolio.append(st)
        self.label_stockprice.setText("Stock Price: " + str(st.share_price))
        self.label_roi.setText("ROE:" + str(st.roe))
        self.label_debtequity.setText("D/E Ratio: " + str(st.debt_equity[len(st.debt_equity)-1]))
        #self.label_debtequity.setText("D/E Ratio: " + str(st.debt_equity(len(st.debt_equity)-1)))
        self.label_netprofitmargin.setText("Net Profit Margin: " + str(st.npm))
        self.label_revenue.setText("Revenue: " + str(st.revenue_info))
        self.label_recommendation.setText("Recommendation: " + st.recommend)
       
        #self.matplotlibwidget_6.
        #self.ui.mplwidget.canvas.fig.tight_layout()

#the below code opens a new window after "show graph" button is clicked
    def ShowGraph(self):
        """        
        app = QtGui.QApplication(sys.argv)
        widget = pg.PlotWidget(title="Stock Performance")
        widget.setWindowTitle("Graph")
        widget.plotItem.plot(floatStockClosePrice)
        """        
        ticker = str(self.lineEdit.text())
        if self.radioButton_3.isChecked() or self.radioButton_4.isChecked() and ticker in theTickers:
            
            widget = pg.plot(floatStockClosePrice, title="Graph")       
                
            ax = widget.getPlotItem().getAxis("left")
            ax.setLabel("Price")
            ax.setGrid(200)
            ax.showLabel()
            
            ax = widget.getPlotItem().getAxis("bottom")
            ax.setLabel("Year")
            ax.setGrid(200)
            ax.showLabel()
                
            widget.show()           
        
        else:
            Tkinter.Tk().withdraw()
            tkMessageBox.showerror("Error: Stock Not Found", "Please try again and click 'See Projection' for graph to show.")

from matplotlibwidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
   
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.raise_()
    MainWindow.show()
    MainWindow.setWindowState(MainWindow.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
    MainWindow.activateWindow()
    sys.exit(app.exec_())
