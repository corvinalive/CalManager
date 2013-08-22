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

        self.connect(self.ui.PMIAddButton, QtCore.SIGNAL("clicked(bool)"), self.pmi_add_button_clicked)
        self.connect(self.ui.PMIDeleteButton, QtCore.SIGNAL("clicked(bool)"), self.pmi_delete_button_clicked)

        self.connect(self.ui.tAddButton, QtCore.SIGNAL("clicked(bool)"), self.t_add_button_clicked)
        self.connect(self.ui.tDeleteButton, QtCore.SIGNAL("clicked(bool)"), self.t_delete_button_clicked)

        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.ok_button_clicked)
               
    def Prepare(self):

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
                tvi.setText(i[0])
            else:
                tvi=QtGui.QTableWidgetItem(i[0])
                self.ui.PovTableWidget.setItem(counter,0,tvi)

            tvi=self.ui.PovTableWidget.item(counter,1)
            if tvi:
                tvi.setText(i[1])
            else:
                tvi=QtGui.QTableWidgetItem(i[1])
                self.ui.PovTableWidget.setItem(counter,1,tvi)

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

        #Заполнение списка методик ДД
        self.ui.PMITableWidget.setRowCount(len(self.Commondata.PMI))
        counter=0
        for i in self.Commondata.PMI:
            #short name
            tvi=self.ui.PMITableWidget.item(counter,0)
            if tvi:
                tvi.setText(i[0])
            else:
                tvi=QtGui.QTableWidgetItem(i[0])
                self.ui.PMITableWidget.setItem(counter,0,tvi)
            #str1
            tvi=self.ui.PMITableWidget.item(counter,1)
            if tvi:
                tvi.setText(i[1])
            else:
                tvi=QtGui.QTableWidgetItem(i[1])
                self.ui.PMITableWidget.setItem(counter,1,tvi)
            #str2
            tvi=self.ui.PMITableWidget.item(counter,2)
            if tvi:
                tvi.setText(i[2])
            else:
                tvi=QtGui.QTableWidgetItem(i[2])
                self.ui.PMITableWidget.setItem(counter,2,tvi)
            #str3
            tvi=self.ui.PMITableWidget.item(counter,3)
            if tvi:
                tvi.setText(i[3])
            else:
                tvi=QtGui.QTableWidgetItem(i[3])
                self.ui.PMITableWidget.setItem(counter,3,tvi)

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

    def pmi_add_button_clicked (self,bool):
        self.ui.PMITableWidget.setRowCount(self.ui.PMITableWidget.rowCount()+1)
        
    def pmi_delete_button_clicked (self,bool):
        i = self.ui.PMITableWidget.currentRow()
        self.ui.PMITableWidget.removeRow(i)
        
    def t_add_button_clicked (self,bool):
        self.ui.tTableWidget.setRowCount(self.ui.tTableWidget.rowCount()+1)

    def t_delete_button_clicked (self,bool):
        i = self.ui.tTableWidget.currentRow()
        self.ui.tTableWidget.removeRow(i)
        
    def add_button_clicked (self,bool):
        self.ui.CompanyTableWidget.setRowCount(self.ui.CompanyTableWidget.rowCount()+1)

    def ok_button_clicked (self):
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
            Name=self.ui.PovTableWidget.item(i,0).text()
            TrustNo=self.ui.PovTableWidget.item(i,1).text()
            self.Commondata.Poveriteli.append((Name,TrustNo))
        #Запись списка PModeli
        c=self.ui.PTableWidget.rowCount()
        self.Commondata.PModeli=[]
        for i in range(c):
            self.Commondata.PModeli.append(self.ui.PTableWidget.item(i,0).text())
        #Запись списка методик ДД
        c=self.ui.PMITableWidget.rowCount()
        self.Commondata.PMI=[]
        for i in range(c):
            Name=self.ui.PMITableWidget.item(i,0).text()
            if self.ui.PMITableWidget.item(i,1) is None:
                String1=""
            else:
                String1=self.ui.PMITableWidget.item(i,1).text()

            if self.ui.PMITableWidget.item(i,2) is None:
                String2=""
            else:
                String2=self.ui.PMITableWidget.item(i,2).text()
                
            if self.ui.PMITableWidget.item(i,3) is None:
                String3=""
            else:
                String3=self.ui.PMITableWidget.item(i,3).text()

            self.Commondata.PMI.append((Name,String1,String2,String3))
        #Запись списка tModeli
        c=self.ui.tTableWidget.rowCount()
        self.Commondata.tModeli=[]
        for i in range(c):
            self.Commondata.tModeli.append(self.ui.tTableWidget.item(i,0).text())
        self.Commondata.SaveSetting()

