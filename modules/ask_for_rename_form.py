# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ask_for_rename_form.ui'
#
# Created: Fri Feb 24 00:06:43 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(711, 379)
        Dialog.setSizeGripEnabled(True)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.FileNameLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.FileNameLabel.setFont(font)
        self.FileNameLabel.setObjectName("FileNameLabel")
        self.gridLayout.addWidget(self.FileNameLabel, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.FolderLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.FolderLabel.setFont(font)
        self.FolderLabel.setObjectName("FolderLabel")
        self.gridLayout.addWidget(self.FolderLabel, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.CancelpushButton = QtGui.QPushButton(Dialog)
        self.CancelpushButton.setObjectName("CancelpushButton")
        self.gridLayout.addWidget(self.CancelpushButton, 5, 0, 1, 1)
        self.RenameNewpushButton = QtGui.QPushButton(Dialog)
        self.RenameNewpushButton.setObjectName("RenameNewpushButton")
        self.gridLayout.addWidget(self.RenameNewpushButton, 7, 0, 1, 1)
        self.RenameOldpushButton = QtGui.QPushButton(Dialog)
        self.RenameOldpushButton.setObjectName("RenameOldpushButton")
        self.gridLayout.addWidget(self.RenameOldpushButton, 8, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 10, 0, 1, 1)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 11, 0, 1, 1)
        self.ReplacepushButton = QtGui.QPushButton(Dialog)
        self.ReplacepushButton.setObjectName("ReplacepushButton")
        self.gridLayout.addWidget(self.ReplacepushButton, 6, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Установка загруженных шаблонов", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "При перемещении загруженного файла", None, QtGui.QApplication.UnicodeUTF8))
        self.FileNameLabel.setText(QtGui.QApplication.translate("Dialog", "filename", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "в папку", None, QtGui.QApplication.UnicodeUTF8))
        self.FolderLabel.setText(QtGui.QApplication.translate("Dialog", "Шаблоны температуры", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "выяснилось, что в этой папке существует файл с таким именем. Возможные варианты действий:", None, QtGui.QApplication.UnicodeUTF8))
        self.CancelpushButton.setText(QtGui.QApplication.translate("Dialog", "&1. Отменить перемещение загруженного файла", None, QtGui.QApplication.UnicodeUTF8))
        self.RenameNewpushButton.setText(QtGui.QApplication.translate("Dialog", "&3. Сохранить загруженный файл под другим именем:", None, QtGui.QApplication.UnicodeUTF8))
        self.RenameOldpushButton.setText(QtGui.QApplication.translate("Dialog", "&4. Переименовать существующий файл:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Имя файла для 3 или 4 го варинта:", None, QtGui.QApplication.UnicodeUTF8))
        self.ReplacepushButton.setText(QtGui.QApplication.translate("Dialog", "&2. Заместить существующий файл", None, QtGui.QApplication.UnicodeUTF8))

