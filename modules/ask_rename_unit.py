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

from ask_for_rename_form import Ui_Dialog

class RenameForm(QtGui.QDialog):
    def __init__(self,cd,parent=None):
        super(RenameForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.Commondata = cd
        self.connect(self.ui.RenameOldpushButton, QtCore.SIGNAL("clicked(bool)"), self.RenameOldpushButton)
        self.connect(self.ui.RenameNewpushButton, QtCore.SIGNAL("clicked(bool)"), self.RenameNewpushButton)
        self.connect(self.ui.CancelpushButton, QtCore.SIGNAL("clicked(bool)"), self.CancelpushButton)
        self.connect(self.ui.ReplacepushButton, QtCore.SIGNAL("clicked(bool)"), self.ReplacepushButton)
        #CancelpushButton   RenameNewpushButton RenameOldpushButton ReplacepushButton
        #lineEdit   FileNameLabel   FolderLabel 

    def Prepare(self,folder, fn):
        self.ui.FolderLabel.setText(folder)
        self.ui.FileNameLabel.setText(fn)
        self.ui.lineEdit.setText(fn)
        
        self.folder=folder
        self.fn=fn
        
        self.answer=-1
             
    def CancelpushButton(self,bool):
        print "cancel"
        self.accept()
        
    def RenameNewpushButton(self,bool):
        print "rename new file"
        new_full_name=os.path.join(self.folder,self.ui.lineEdit.text())
        if os.path.exists(new_full_name)==False:
            self.answer=1
            self.accept()
        else:
            self.ui.label.setText(u"Файл с таким именем существует. Введите другое имя файла")

    def ReplacepushButton(self,bool):
        print "replace new file"
        self.answer=3
        self.accept()

    def RenameOldpushButton(self,bool):
        print "rename old file"
        new_full_name=os.path.join(self.folder,self.ui.lineEdit.text())
        if os.path.exists(new_full_name)==False:
            self.answer=2
            self.accept()
        else:
            self.ui.label.setText(u"Файл с таким именем существует. Введите другое имя файла")
