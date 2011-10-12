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
from press_unit import PressForm
import commondata

class MyMainWindow(QtGui.QMainWindow):
           
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MyMainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.mdiArea);
        self.connect(self.ui.Tempaction, QtCore.SIGNAL("triggered()"), self.pushButtonTemp)
        self.connect(self.ui.Pressaction, QtCore.SIGNAL("triggered()"), self.pushButtonPress)
        self.connect(self.ui.Aboutaction, QtCore.SIGNAL("triggered()"), self.aboutButton)
        self.Commondata = commondata.Commondata()
    
      
    def pushButtonTemp(self):
        tempform1 = TempForm(self.Commondata,self)
        self.ui.mdiArea.addSubWindow(tempform1)
        tempform1.show()
    def pushButtonPress(self):
        pressform1 = PressForm(self.Commondata,self)
        self.ui.mdiArea.addSubWindow(pressform1)
        pressform1.show()
    def aboutButton(self):
        QtGui.QMessageBox.about(self, u"Поверка датчиков давления и температуры",
                u"Программа для обработки данных и формирования свидетельств и протоколов поверки датчиков давления и \
                температуры.\n\nАвтор: Зонов В. М.\n\ne-mail: corvinalive@list.ru\n\nЛицензия: GPL v.2\n\n\
                Исходники: https://corvinalive@github.com/corvinalive/CalManager.git\n\nВерсия: 0.4 betta")

        
		    

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()
    result=app.exec_()
    sys.exit(result)
    return 0

if __name__ == '__main__':
	main()

