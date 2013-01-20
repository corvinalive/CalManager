# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/update_form.ui'
#
# Created: Sun Jan 20 22:06:59 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(998, 661)
        Dialog.setSizeGripEnabled(True)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.listWidget1 = QtGui.QListWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.listWidget1.sizePolicy().hasHeightForWidth())
        self.listWidget1.setSizePolicy(sizePolicy)
        self.listWidget1.setObjectName("listWidget1")
        self.gridLayout.addWidget(self.listWidget1, 2, 0, 1, 1)
        self.listWidget2 = QtGui.QListWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.listWidget2.sizePolicy().hasHeightForWidth())
        self.listWidget2.setSizePolicy(sizePolicy)
        self.listWidget2.setObjectName("listWidget2")
        self.gridLayout.addWidget(self.listWidget2, 2, 1, 1, 1)
        self.CheckpushButton = QtGui.QPushButton(Dialog)
        self.CheckpushButton.setObjectName("CheckpushButton")
        self.gridLayout.addWidget(self.CheckpushButton, 6, 0, 1, 2)
        self.LoadpushButton = QtGui.QPushButton(Dialog)
        self.LoadpushButton.setObjectName("LoadpushButton")
        self.gridLayout.addWidget(self.LoadpushButton, 7, 0, 1, 2)
        self.addpushButton = QtGui.QPushButton(Dialog)
        self.addpushButton.setObjectName("addpushButton")
        self.gridLayout.addWidget(self.addpushButton, 4, 0, 1, 1)
        self.deletepushButton = QtGui.QPushButton(Dialog)
        self.deletepushButton.setObjectName("deletepushButton")
        self.gridLayout.addWidget(self.deletepushButton, 4, 1, 1, 1)
        self.Statuslabel = QtGui.QLabel(Dialog)
        self.Statuslabel.setObjectName("Statuslabel")
        self.gridLayout.addWidget(self.Statuslabel, 8, 0, 1, 2)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Обновление. Текущая версия 0.4", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Список загрузки:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Доступные:", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckpushButton.setText(QtGui.QApplication.translate("Dialog", "Проверить обновления", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadpushButton.setText(QtGui.QApplication.translate("Dialog", "Загрузить выбранное", None, QtGui.QApplication.UnicodeUTF8))
        self.addpushButton.setText(QtGui.QApplication.translate("Dialog", "Добавить в список загрузки", None, QtGui.QApplication.UnicodeUTF8))
        self.deletepushButton.setText(QtGui.QApplication.translate("Dialog", "Удалить из списка загрузки", None, QtGui.QApplication.UnicodeUTF8))
        self.Statuslabel.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">СТАТУС:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Инструкция по обновлению:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Нажать кнопку &quot;<span style=\" font-style:italic; text-decoration: underline;\">Проверить обновления</span>&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">В левой колонке появится список доступных файлов для обновления.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Кнопками &quot;<span style=\" font-style:italic; text-decoration: underline;\">Добавить в список загрузки</span>&quot; и &quot;<span style=\" font-style:italic; text-decoration: underline;\">Удалить из списка загрузки</span>&quot; выбрать файлы для скачивания.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Нажать кнопку &quot;<span style=\" font-style:italic; text-decoration: underline;\">Загрузить выбранное</span>&quot;. В случае успешной загрузки шаблоны будут сохранены в нужных папках, новые версии ПО сохранятся в папке с программой в архиве, который нужно будет распаковать в папку с программой. При рапаковке архива ответить утвердительно на вопрос о замещении файлов новыми.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

