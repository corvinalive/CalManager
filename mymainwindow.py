# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mymainwindow.ui'
#
# Created: Wed Sep 14 12:55:55 2011
#      by: pyside-uic 0.2.8 running on PySide 1.0.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MyMainWindow(object):
    def setupUi(self, MyMainWindow):
        MyMainWindow.setObjectName("MyMainWindow")
        MyMainWindow.resize(791, 600)
        MyMainWindow.setDocumentMode(True)
        self.centralwidget = QtGui.QWidget(MyMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(120, 160, 200, 160))
        self.mdiArea.setObjectName("mdiArea")
        MyMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MyMainWindow)
        self.statusbar.setObjectName("statusbar")
        MyMainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MyMainWindow)
        self.toolBar.setObjectName("toolBar")
        MyMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MyMainWindow.insertToolBarBreak(self.toolBar)
        self.Tempaction = QtGui.QAction(MyMainWindow)
        self.Tempaction.setVisible(True)
        self.Tempaction.setIconVisibleInMenu(False)
        self.Tempaction.setObjectName("Tempaction")
        self.Pressaction = QtGui.QAction(MyMainWindow)
        self.Pressaction.setObjectName("Pressaction")
        self.Setupaction = QtGui.QAction(MyMainWindow)
        self.Setupaction.setObjectName("Setupaction")
        self.Aboutaction = QtGui.QAction(MyMainWindow)
        self.Aboutaction.setObjectName("Aboutaction")
        self.toolBar.addAction(self.Tempaction)
        self.toolBar.addAction(self.Pressaction)
        self.toolBar.addAction(self.Setupaction)
        self.toolBar.addAction(self.Aboutaction)

        self.retranslateUi(MyMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MyMainWindow)

    def retranslateUi(self, MyMainWindow):
        MyMainWindow.setWindowTitle(QtGui.QApplication.translate("MyMainWindow", "CalManager 0.4", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MyMainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.Tempaction.setText(QtGui.QApplication.translate("MyMainWindow", "Температура", None, QtGui.QApplication.UnicodeUTF8))
        self.Pressaction.setText(QtGui.QApplication.translate("MyMainWindow", "Давление", None, QtGui.QApplication.UnicodeUTF8))
        self.Setupaction.setText(QtGui.QApplication.translate("MyMainWindow", "Настройка", None, QtGui.QApplication.UnicodeUTF8))
        self.Aboutaction.setText(QtGui.QApplication.translate("MyMainWindow", "О программе...", None, QtGui.QApplication.UnicodeUTF8))

