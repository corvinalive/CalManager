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

from options import Ui_OptionsDialog

class OptionsForm(QtGui.QDialog):
    def __init__(self,cd,parent=None):
        super(OptionsForm, self).__init__(parent)
        self.ui = Ui_OptionsDialog()
        self.ui.setupUi(self)
        self.Commondata = cd
        self.ui.CompanyTableWidget.setColumnWidth(1,150)
        self.ui.CompanyTableWidget.setColumnWidth(0,350)

        self.connect(self.ui.AddButton, QtCore.SIGNAL("clicked(bool)"), self.add_button_clicked)
        self.connect(self.ui.DeleteButton, QtCore.SIGNAL("clicked(bool)"), self.delete_button_clicked)

        self.connect(self.ui.AddPovButton, QtCore.SIGNAL("clicked(bool)"), self.pov_add_button_clicked)
        self.connect(self.ui.DeletePovButton, QtCore.SIGNAL("clicked(bool)"), self.pov_delete_button_clicked)

        self.connect(self.ui.PAddButton, QtCore.SIGNAL("clicked(bool)"), self.p_add_button_clicked)
        self.connect(self.ui.PDeleteButton, QtCore.SIGNAL("clicked(bool)"), self.p_delete_button_clicked)

        self.connect(self.ui.tAddButton, QtCore.SIGNAL("clicked(bool)"), self.t_add_button_clicked)
        self.connect(self.ui.tDeleteButton, QtCore.SIGNAL("clicked(bool)"), self.t_delete_button_clicked)

        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.ok_button_clicked)
               
    def Prepare(self):
        print "Prepare"
        self.ui.CompanyTableWidget.setRowCount(len(self.Commondata.Companies))
        counter=0
        for i in self.Commondata.Companies:
            tvi=self.ui.CompanyTableWidget.item(counter,0)
            if tvi:
                tvi.setText(i[0])
            else:
                tvi=QtGui.QTableWidgetItem(i[0])
                self.ui.CompanyTableWidget.setItem(counter,0,tvi)

            tvi=self.ui.CompanyTableWidget.item(counter,1)
            if tvi:
                tvi.setText(i[1])
            else:
                tvi=QtGui.QTableWidgetItem(i[1])
                self.ui.CompanyTableWidget.setItem(counter,1,tvi)
            
            counter+=1
        #Заполнение списка поверителй
        self.ui.PovTableWidget.setRowCount(len(self.Commondata.Poveriteli))
        counter=0
        for i in self.Commondata.Poveriteli:
            tvi=self.ui.PovTableWidget.item(counter,0)
            if tvi:
                tvi.setText(i)
            else:
                tvi=QtGui.QTableWidgetItem(i)
                self.ui.PovTableWidget.setItem(counter,0,tvi)
            counter+=1
        #Заполнение списка PModeli
        self.ui.PTableWidget.setRowCount(len(self.Commondata.PModeli))
        counter=0
        for i in self.Commondata.PModeli:
            tvi=self.ui.PTableWidget.item(counter,0)
            if tvi:
                tvi.setText(i)
            else:
                tvi=QtGui.QTableWidgetItem(i)
                self.ui.PTableWidget.setItem(counter,0,tvi)
            counter+=1
        #Заполнение списка tModeli
        self.ui.tTableWidget.setRowCount(len(self.Commondata.tModeli))
        counter=0
        for i in self.Commondata.tModeli:
            tvi=self.ui.tTableWidget.item(counter,0)
            if tvi:
                tvi.setText(i)
            else:
                tvi=QtGui.QTableWidgetItem(i)
                self.ui.tTableWidget.setItem(counter,0,tvi)
            counter+=1
        #Сервер
        self.ui.ServerEdit.setText(self.Commondata.servername)

    def delete_button_clicked (self,bool):
        i = self.ui.CompanyTableWidget.currentRow()
        self.ui.CompanyTableWidget.removeRow(i)
        
    def pov_delete_button_clicked (self, bool):
        i = self.ui.PovTableWidget.currentRow()
        self.ui.PovTableWidget.removeRow(i)
        
    def pov_add_button_clicked (self, bool):
        self.ui.PovTableWidget.setRowCount(self.ui.PovTableWidget.rowCount()+1)
    
    def p_delete_button_clicked (self, bool):
        i = self.ui.PTableWidget.currentRow()
        self.ui.PTableWidget.removeRow(i)
        
    def p_add_button_clicked (self,bool):
        self.ui.PTableWidget.setRowCount(self.ui.PTableWidget.rowCount()+1)
        
    def t_delete_button_clicked (self,bool):
        i = self.ui.tTableWidget.currentRow()
        self.ui.tTableWidget.removeRow(i)
        
    def t_add_button_clicked (self,bool):
        self.ui.tTableWidget.setRowCount(self.ui.tTableWidget.rowCount()+1)
        
    def add_button_clicked (self,bool):
        self.ui.CompanyTableWidget.setRowCount(self.ui.CompanyTableWidget.rowCount()+1)

    def ok_button_clicked (self):
        print "Ok button pressed"
        #Save changes
        self.Commondata.servername=self.ui.ServerEdit.text()
        c=self.ui.CompanyTableWidget.rowCount()
        self.Commondata.Companies=[]
        for i in range(c):
            Name=self.ui.CompanyTableWidget.item(i,0).text()
            INN=self.ui.CompanyTableWidget.item(i,1).text()
            self.Commondata.Companies.append((Name,INN))
        #Запись списка поверителей
        c=self.ui.PovTableWidget.rowCount()
        self.Commondata.Poveriteli=[]
        for i in range(c):
            self.Commondata.Poveriteli.append(self.ui.PovTableWidget.item(i,0).text())
        #Запись списка PModeli
        c=self.ui.PTableWidget.rowCount()
        self.Commondata.PModeli=[]
        for i in range(c):
            self.Commondata.PModeli.append(self.ui.PTableWidget.item(i,0).text())
        #Запись списка tModeli
        c=self.ui.tTableWidget.rowCount()
        self.Commondata.tModeli=[]
        for i in range(c):
            self.Commondata.tModeli.append(self.ui.tTableWidget.item(i,0).text())
        self.Commondata.SaveSetting()

