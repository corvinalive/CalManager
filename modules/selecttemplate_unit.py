#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       options_unit.py
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

import struct, sys, os
from PySide import QtCore, QtGui
import commondata

from SelectTemplateDiaog import Ui_SelectTemplateDialog

class SelectTemplate(QtGui.QDialog):
    def __init__(self,cd,parent=None):
        super(SelectTemplate, self).__init__(parent)
        self.ui = Ui_SelectTemplateDialog()
        self.ui.setupUi(self)
        self.Commondata = cd

        self.connect(self.ui.TemplateList, QtCore.SIGNAL("currentRowChanged(int)"), self.row_changed)
        self.connect(self.ui.TemplateList, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.dblclick)

    def dblclick(self,lwi):
        self.accept()
         

    def Select(self,Templates,index):
        if len(Templates)<1:
            return ("",-1)

        if len(Templates)==1:
            return ((Templates[0])[1],0)
            
        self.ui.TemplateList.clear()
        for f in Templates:
            lwi = QtGui.QListWidgetItem(f[0])
            lwi.setData(QtCore.Qt.UserRole, f)
            self.ui.TemplateList.addItem(lwi)
        if index<0:
            index=0

        if(index >= len(Templates)):
            index=0

        self.ui.TemplateList.setCurrentRow(index)
        self.fn=""
        if (self.exec_() > 0):
            return  (self.ui.TemplateList.currentItem().data(QtCore.Qt.UserRole)[1],self.ui.TemplateList.currentRow())
        else:
            return None

    def row_changed(self, Row):
        index=Row
        if index<0:
            self.ui.label.setText("")

        self.ui.label.setText(self.ui.TemplateList.item(index).data(QtCore.Qt.UserRole)[2])
        
def main():
    return 0	
    

if __name__ == '__main__':
    main()

