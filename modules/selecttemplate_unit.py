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

        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.ok_button_clicked)

    def Select(self,TemplateDir):
        print "Select in ",TemplateDir
        filelist = os.listdir(TemplateDir)
        filelistlen=len(filelist)
        if  filelistlen==0 :
            return
        self.ui.TemplateList.clear()
        for f in filelist:
            print f
            if f.endswith(u".odt"):
                lbl=os.path.split(f)[1]
                lbl=os.path.splitext(lbl)[0]
                lwi = QtGui.QListWidgetItem(lbl)
                lwi.setData(QtCore.Qt.UserRole, os.path.join(TemplateDir,f))
                self.ui.TemplateList.addItem(lwi)
        self.exec_()
               
    def Prepare(self):
        print "Prepare select template"

    def ok_button_clicked (self):
        si= self.ui.TemplateList.selectedItems()
        for sii in si:
            print sii.data(QtCore.Qt.UserRole)
        print "Select template ok"

