# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ask12.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_XML_Win(object):
    def setupUi(self, XML_Win):
        XML_Win.setObjectName("XML_Win")
        XML_Win.resize(400, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(XML_Win.sizePolicy().hasHeightForWidth())
        XML_Win.setSizePolicy(sizePolicy)
        XML_Win.setMinimumSize(QtCore.QSize(400, 400))
        XML_Win.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(XML_Win)
        self.centralwidget.setObjectName("centralwidget")
        self.xml_input = QtWidgets.QPushButton(self.centralwidget)
        self.xml_input.setGeometry(QtCore.QRect(20, 170, 75, 23))
        self.xml_input.setObjectName("xml_input")
        self.xsd_input = QtWidgets.QPushButton(self.centralwidget)
        self.xsd_input.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.xsd_input.setObjectName("xsd_input")
        self.Data = QtWidgets.QTableView(self.centralwidget)
        self.Data.setGeometry(QtCore.QRect(10, 210, 381, 171))
        self.Data.setAutoFillBackground(False)
        self.Data.setShowGrid(True)
        self.Data.setObjectName("Data")
        self.Lesson = QtWidgets.QLabel(self.centralwidget)
        self.Lesson.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.Lesson.setObjectName("Lesson")
        self.Professor = QtWidgets.QLabel(self.centralwidget)
        self.Professor.setGeometry(QtCore.QRect(20, 70, 61, 21))
        self.Professor.setObjectName("Professor")
        self.Day = QtWidgets.QLabel(self.centralwidget)
        self.Day.setGeometry(QtCore.QRect(20, 110, 51, 21))
        self.Day.setObjectName("Day")
        self.Lesson_val = QtWidgets.QLineEdit(self.centralwidget)
        self.Lesson_val.setGeometry(QtCore.QRect(80, 30, 131, 20))
        self.Lesson_val.setObjectName("Lesson_val")
        self.Professor_val = QtWidgets.QLineEdit(self.centralwidget)
        self.Professor_val.setGeometry(QtCore.QRect(80, 70, 131, 20))
        self.Professor_val.setObjectName("Professor_val")
        self.Day_val = QtWidgets.QLineEdit(self.centralwidget)
        self.Day_val.setGeometry(QtCore.QRect(80, 110, 131, 20))
        self.Day_val.setObjectName("Day_val")
        self.add_to_xml = QtWidgets.QPushButton(self.centralwidget)
        self.add_to_xml.setGeometry(QtCore.QRect(240, 70, 75, 23))
        self.add_to_xml.setObjectName("add_to_xml")
        self.filter = QtWidgets.QComboBox(self.centralwidget)
        self.filter.setGeometry(QtCore.QRect(200, 180, 91, 22))
        self.filter.setEditable(False)
        self.filter.setObjectName("filter")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(300, 180, 75, 23))
        self.submit.setObjectName("submit")
        XML_Win.setCentralWidget(self.centralwidget)

        self.retranslateUi(XML_Win)
        QtCore.QMetaObject.connectSlotsByName(XML_Win)

    def retranslateUi(self, XML_Win):
        _translate = QtCore.QCoreApplication.translate
        XML_Win.setWindowTitle(_translate("XML_Win", "Επεξεργασία XML αρχείων"))
        self.xml_input.setText(_translate("XML_Win", "XML File"))
        self.xsd_input.setText(_translate("XML_Win", "XSD File"))
        self.Lesson.setText(_translate("XML_Win", "Lesson:"))
        self.Professor.setText(_translate("XML_Win", "Professor:"))
        self.Day.setText(_translate("XML_Win", "Day:"))
        self.add_to_xml.setText(_translate("XML_Win", "Add"))
        self.filter.setItemText(0, _translate("XML_Win", "Monday"))
        self.filter.setItemText(1, _translate("XML_Win", "Tuesday"))
        self.filter.setItemText(2, _translate("XML_Win", "Wednesday"))
        self.filter.setItemText(3, _translate("XML_Win", "Thursday"))
        self.filter.setItemText(4, _translate("XML_Win", "Friday"))
        self.filter.setItemText(5, _translate("XML_Win", "All Days"))
        self.submit.setText(_translate("XML_Win", "Submit"))
