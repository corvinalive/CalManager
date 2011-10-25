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
import ftplib

from update_form import Ui_Dialog

class UpdateForm(QtGui.QDialog):
    def __init__(self,cd,parent=None):
        super(UpdateForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.Commondata = cd
        self.connect(self.ui.CheckpushButton, QtCore.SIGNAL("clicked(bool)"), self.CheckUpdatesButton)
        self.connect(self.ui.addpushButton, QtCore.SIGNAL("clicked(bool)"), self.AddButton)
        self.connect(self.ui.deletepushButton, QtCore.SIGNAL("clicked(bool)"), self.DeleteButton)
        self.connect(self.ui.LoadpushButton, QtCore.SIGNAL("clicked(bool)"), self.LoadButton)
    
    def LoadButton(self):
        print "Load"
        c = self.ui.listWidget2.count()
        if c==0:
            self.ui.Statuslabel.setText(u"Ничего не выбрано для загрузкиs")
            return
        for i in range(c):
            fn=self.ui.listWidget2.item(i).data(1)
                
    def AddButton(self):
        item=self.ui.listWidget1.currentItem()
        if item:
            print "item"
        else:
            return
        if item.data(1)==None:
            print "data==None"
            return
        
        c = self.ui.listWidget2.count()
        for i in range(c):
            if self.ui.listWidget2.item(i).data(1)==item.data(1):
                return
        item2 = QtGui.QListWidgetItem(item.text())
        item2.setData(1,item.data(1))
        self.ui.listWidget2.addItem(item2)        

    def DeleteButton(self):
        item=self.ui.listWidget2.currentItem()
        self.ui.listWidget2.removeItemWidget(item)
        
        
        
    def CheckUpdatesButton(self):
        """
        fn=[]
        fn.append(("calmanager/press_templates/list","press_list"))
        fn.append(("calmanager/temp_templates/list","temp_list"))
        fn.append(("calmanager/windows_binary/list","windows_list"))
        fn.append(("calmanager/linux_binary/list","linux_list"))
        server = "ims-nv.ru"
        try:
            ftp = ftplib.FTP(server,timeout=30)
            ftp.login()
            for fni in fn:
                print "Get file ", fni[0]
                ftp.retrbinary("RETR "+fni[0], open(fni[1], "w+").write)
            ftp.quit()
            self.ui.Statuslabel.setText(u"Обновления загружены")
        except ftplib.all_errors, err:
            #s=u"Ошибка проверки: "
            #ss= str(err).decode("utf-8")
            #s+=ss
            self.ui.Statuslabel.setText(u"Ошибка проверки: "+str(err).decode("utf-8"))
        """    
        self.ShowUpdates()
        
    def ReadList(self,filename,outlist):
        fn = open(filename)
        fname=""
        fdescr=""
        fnamesetted=False

        lines = fn.readlines()
        for line in lines:
            if line.startswith("#"):
                continue
            if line.isspace():
                continue
            if fnamesetted==False:
                fname=line.strip()
                fnamesetted=True
            else:
                fdescr=line.strip()
                fnamesetted=False
                outlist.append((fname,fdescr))
        fn.close()
        
    def ShowUpdates(self):
        #read press list
        self.presslist=[]
        self.ReadList("press_list",self.presslist)
        self.templist=[]
        self.ReadList("temp_list",self.templist)
        self.wpolist=[]
        self.ReadList("windows_list",self.wpolist)
        self.lpolist=[]
        self.ReadList("linux_list",self.lpolist)
        
        self.ui.listWidget1.clear()
        #add pressure items
        self.ui.listWidget1.addItem(u"Шаблоны давления:")
        for i in self.presslist:
            item = QtGui.QListWidgetItem(i[1].decode("utf8"))
            item.setData(1,i[0].decode("utf8"))
            self.ui.listWidget1.addItem(item)
        #add temp items
        self.ui.listWidget1.addItem(u"Шаблоны температуры:")
        for i in self.templist:
            item = QtGui.QListWidgetItem(i[1].decode("utf8"))
            item.setData(1,i[0].decode("utf8"))
            self.ui.listWidget1.addItem(item)
        #add win items
        self.ui.listWidget1.addItem(u"Программа для Windows:")
        for i in self.wpolist:
            item = QtGui.QListWidgetItem(i[1].decode("utf8"))
            item.setData(1,i[0].decode("utf8"))
            self.ui.listWidget1.addItem(item)
        #add linux items
        self.ui.listWidget1.addItem(u"Программа для Linux:")
        for i in self.lpolist:
            item = QtGui.QListWidgetItem(i[1].decode("utf8"))
            item.setData(1,i[0].decode("utf8"))
            self.ui.listWidget1.addItem(item)



def main():
    print "main"


    
    
    return 0	
    

if __name__ == '__main__':
    main()
               
