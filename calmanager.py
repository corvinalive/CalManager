#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       calmanager.py
#       
#       Copyright 2011 Zonov Valerij <corvinalive@list.ru>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
   
import struct, sys
from PySide import QtCore, QtGui
from mymainwindow import Ui_MyMainWindow
from temp_unit import TempForm
import ConfigParser

class MyMainWindow(QtGui.QMainWindow):
           
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MyMainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.mdiArea);
        self.connect(self.ui.Tempaction, QtCore.SIGNAL("triggered()"), self.pushButtonTemp)
        self.connect(self.ui.Aboutaction, QtCore.SIGNAL("triggered()"), self.aboutButton)
        self.LoadSetting()
    
    def LoadSetting(self):
        print "Load setting"
        qs = QtCore.QSettings("calmanager.ini", QtCore.QSettings.IniFormat)
        size = qs.beginReadArray("companies")
        self.Companies=[]
        for i in range(size):
            qs.setArrayIndex(i)
            Name = qs.value("Name")
            INN= qs.value("INN")
            print Name, INN
            self.Companies.append((Name,INN))
        qs.endArray()

        size = qs.beginReadArray("poveriteli")
        self.Poveriteli=[]
        for i in range(size):
            qs.setArrayIndex(i)
            Name = qs.value("FIO")
            print Name
            self.Poveriteli.append(Name)
        qs.endArray()

        size = qs.beginReadArray("PModeli")
        self.PModeli=[]
        for i in range(size):
            qs.setArrayIndex(i)
            Name = qs.value("FIO")
            print Name
            self.PModeli.append(Name)
        qs.endArray()

        size = qs.beginReadArray("tModeli")
        self.tModeli=[]
        for i in range(size):
            qs.setArrayIndex(i)
            Name = qs.value("FIO")
            print Name
            self.tModeli.append(Name)
        qs.endArray()

      
    def pushButtonTemp(self):
        tempform1 = TempForm(self)
        self.ui.mdiArea.addSubWindow(tempform1)
        tempform1.show()
    def aboutButton(self):
        QtGui.QMessageBox.about(self, u"Поверка датчиков давления и температуры",
                u"Программа для обработки данных и формирования свидетельств и протоколов поверки датчиков давления и температуры.\n\nАвтор: Зонов В. М.\n\ne-mail: corvinalive@list.ru\n\nЛицензия: GPL v.2\n\nВерсия: 0.4 betta")

        
		    

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()
    result=app.exec_()
    sys.exit(result)
    return 0

if __name__ == '__main__':
	main()

