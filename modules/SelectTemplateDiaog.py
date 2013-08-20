# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SelectTemplateDialog.ui'
#
# Created: Mon Aug 19 23:59:59 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SelectTemplateDialog(object):
    def setupUi(self, SelectTemplateDialog):
        SelectTemplateDialog.setObjectName("SelectTemplateDialog")
        SelectTemplateDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SelectTemplateDialog.resize(712, 463)
        SelectTemplateDialog.setModal(False)
        self.gridLayout = QtGui.QGridLayout(SelectTemplateDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(SelectTemplateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.label = QtGui.QLabel(SelectTemplateDialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.TemplateList = QtGui.QListWidget(SelectTemplateDialog)
        self.TemplateList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.TemplateList.setProperty("showDropIndicator", False)
        self.TemplateList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.TemplateList.setObjectName("TemplateList")
        QtGui.QListWidgetItem(self.TemplateList)
        QtGui.QListWidgetItem(self.TemplateList)
        self.gridLayout.addWidget(self.TemplateList, 0, 0, 1, 1)

        self.retranslateUi(SelectTemplateDialog)
        self.TemplateList.setCurrentRow(-1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SelectTemplateDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SelectTemplateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectTemplateDialog)
        SelectTemplateDialog.setTabOrder(self.TemplateList, self.buttonBox)

    def retranslateUi(self, SelectTemplateDialog):
        SelectTemplateDialog.setWindowTitle(QtGui.QApplication.translate("SelectTemplateDialog", "Выбор шаблона", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SelectTemplateDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.TemplateList.isSortingEnabled()
        self.TemplateList.setSortingEnabled(False)
        self.TemplateList.item(0).setText(QtGui.QApplication.translate("SelectTemplateDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.TemplateList.item(1).setText(QtGui.QApplication.translate("SelectTemplateDialog", "ваыв", None, QtGui.QApplication.UnicodeUTF8))
        self.TemplateList.setSortingEnabled(__sortingEnabled)

