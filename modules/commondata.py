#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Без имени.py
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

from PySide import QtCore
import sys, os, locale
import logging

class Commondata:
    def __init__(self):
        self.LoadSetting()
           
        logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                            level = self.loglevel, filename = u'calmanager.log')
        self.logging = logging
        
        self.version="0.4.1"
        logging.info(u"Calmanager version "+str(self.version))
        
        self.kod1=locale.getpreferredencoding()
        logging.info(u"locale.getpreferredencoding "+str(self.kod1))
        
        self.apppath=sys.path[0].decode(self.kod1,"utf-8")
        logging.info(u"Путь к программе "+self.apppath)
        
        self.press_template_dir=os.path.join(self.apppath,u"Шаблоны давление")
        logging.info(u"press_template_dir "+self.press_template_dir)
        
        self.temp_template_dir=os.path.join(self.apppath,u"Шаблоны температура")
        logging.info(u"temp_template_dir "+self.temp_template_dir)

    def LoadSetting(self):
        #print "Load setting"
        qs = QtCore.QSettings("calmanager.ini", QtCore.QSettings.IniFormat)
        #read name of server
        self.servername=qs.value("update/server","")
        self.loglevel=int(qs.value("update/loglevel",40))
        size = qs.beginReadArray("companies")
        self.Companies=[]
        for i in range(size):
            qs.setArrayIndex(i)
            Name = qs.value("Name")
            INN= qs.value("INN")
            #print Name, INN
            self.Companies.append((Name,INN))
        qs.endArray()

        size = qs.beginReadArray("poveriteli")
        self.Poveriteli=[]
        for i in range(size):
            qs.setArrayIndex(i)
            Name = qs.value("FIO")
            #print Name
            self.Poveriteli.append(Name)
        qs.endArray()

        size = qs.beginReadArray("PModeli")
        self.PModeli=[]
        for i in range(size):
            qs.setArrayIndex(i)
            Name = qs.value("FIO")
            #print Name
            self.PModeli.append(Name)
        qs.endArray()

        size = qs.beginReadArray("tModeli")
        self.tModeli=[]
        for i in range(size):
            qs.setArrayIndex(i)
            Name = qs.value("FIO")
            #print Name
            self.tModeli.append(Name)
        qs.endArray()

    def SaveSetting(self):
        #print "Save setting"
        qs = QtCore.QSettings("calmanager.ini", QtCore.QSettings.IniFormat)
        #save server name
        qs.setValue("update/server", self.servername)
        size = qs.beginWriteArray("companies")
        c = len(self.Companies)
        for i in range(c):
            qs.setArrayIndex(i)
            qs.setValue("Name", self.Companies[i][0])
            qs.setValue("INN", self.Companies[i][1])
        qs.endArray()

        size = qs.beginWriteArray("poveriteli")
        c = len(self.Poveriteli)
        for i in range(c):
            qs.setArrayIndex(i)
            qs.setValue("FIO", self.Poveriteli[i])
        qs.endArray()

        size = qs.beginWriteArray("PModeli")
        c = len(self.PModeli)
        for i in range(c):
            qs.setArrayIndex(i)
            qs.setValue("FIO", self.PModeli[i])
        qs.endArray()

        size = qs.beginWriteArray("tModeli")
        c = len(self.tModeli)
        for i in range(c):
            qs.setArrayIndex(i)
            qs.setValue("FIO", self.tModeli[i])
        qs.endArray()
