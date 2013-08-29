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
        self.kod1=sys.getfilesystemencoding()
        print "kod1= ",self.kod1

        if hasattr(sys, "frozen"):
			self.apppath=os.path.dirname(unicode(sys.executable, sys.getfilesystemencoding( )))
        else:
			self.apppath= unicode(sys.path[0], sys.getfilesystemencoding( ))

        self.LoadSetting()
           
        logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                            level = self.loglevel, filename = u'calmanager.log')
        self.logging = logging
        print logging
        
        self.version="0.5.0"
        logging.info(u"Calmanager version "+str(self.version))
        
        logging.info(u"sys.getfilesystemencoding "+str(self.kod1))
        
        logging.info(u"Путь к программе "+self.apppath)
        
        self.press_template_dir=unicode(os.path.join(self.apppath,unicode(u"Шаблоны давление")))
        logging.info(u"press_template_dir "+self.press_template_dir)
        
        self.temp_template_dir=os.path.join(self.apppath,u"Шаблоны температура")
        logging.info(u"temp_template_dir "+self.temp_template_dir)
        self.PressLastTemplateIndex=-1
        self.TempLastTemplateIndex=-1
        #Загрузка списка шаблонов
        self.PressTemplates=[]
        self.MakeTemplatesList(self.press_template_dir,self.PressTemplates)

        self.TempTemplates=[]
        self.MakeTemplatesList(self.temp_template_dir,self.TempTemplates)
        
    def UnicodeToSystem(self,filename):
        return filename.encode(self.kod1)
    
    def SystemToUnicode(self,filename):
        return unicode(filename,self.kod1)

    def MakeTemplatesList(self,TemplateDir,OutData):
        #Создает списки шаблонов. Каждый элемент содержит имя шаблона,
        #полное имя файла и описание шаблона.
        fn=u""
        filelist = os.listdir(self.UnicodeToSystem(TemplateDir))
        filelistlen=len(filelist)
        if  filelistlen==0 :
            return
        for f in filelist:
            f=self.SystemToUnicode(f)
            if f.endswith(u".odt"):
                lbl=os.path.split(f)[1]
                lbl=os.path.splitext(lbl)[0]
                fullname=os.path.join(TemplateDir,f)
                desc = self.ReadDescription(fullname)
                OutData.append((lbl,fullname,desc))


    def ReadDescription(self,filename):
        #delete temp file
        tempfilename=filename+".temp"
        QtCore.QFile.remove(tempfilename)
        
        #copy to temp
        if ( QtCore.QFile.copy(filename,tempfilename)==False):
            logging.error(u"Чтение описания шаблонов. Ошибка копирования файла "+filename+u" во временный файл "+tempfilename)
            return
        
        #delete content.xml		
        QtCore.QFile.remove(os.path.join(self.apppath,"content.xml"))
        
        arguments = []
        arguments.append(tempfilename)
        arguments.append("content.xml")
        arguments.append(u"-d")
        arguments.append(self.apppath)

        unZip = QtCore.QProcess()
        unZip.start("unzip", arguments)

        if not unZip.waitForFinished(5000):
            logging.error(u"Чтение описания шаблонов. Ошибка извлечения файла <content.xml> из файла "+filename)
            return

        if (unZip.exitCode()<>0) :
            logging.error(u"Чтение описания шаблонов. Ошибка извлечения файла <content.xml> из файла "+filename+u": unzip вернул ненулевой код выхода"+str(unZip.exitCode()))
            return
        QtCore.QFile.remove(tempfilename)
        
        fl = open(self.UnicodeToSystem(os.path.join(self.apppath,"content.xml")))
        flstr = unicode((fl.read()),"Utf8")
        fl.close()

        #delete content.xml		
        QtCore.QFile.remove(self.UnicodeToSystem(os.path.join(self.apppath,"content.xml")))

        b=flstr.find(u"Описание")+9
        if (b-9) < 0:
            return u""
        
        e=flstr.find(u"КонецОписание")-13
        result= flstr[b:e]
        lenstr = len(result)
        result1=u""
        start = 0
        while 1:
            end = result.find("<",start)
            if (end > 0):
                result1 = result1 + result[start:end]
                start = result.find(">",end)+1
                if (start < 1 ):
                    break

        return result1

    def LoadSetting(self):
        #print "Load setting"
        qs = QtCore.QSettings(os.path.join(self.apppath,u"calmanager.ini"), QtCore.QSettings.IniFormat)
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
            Doverennost = qs.value("TrustNo")
            #print Name
            self.Poveriteli.append((Name,Doverennost))
        qs.endArray()

        size = qs.beginReadArray("PModeli")
        self.PModeli=[]
        for i in range(size):
            qs.setArrayIndex(i)
            Name = qs.value("FIO")
            #print Name
            self.PModeli.append(Name)
        qs.endArray()

        size = qs.beginReadArray("PMI")
        self.PMI=[]
        for i in range(size):
            qs.setArrayIndex(i)
            Name = qs.value("MI")
            String1 = qs.value("string1")
            String2 = qs.value("string2")
            String3 = qs.value("string3")
            #print Name
            self.PMI.append((Name,String1,String2,String3))
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
            qs.setValue("FIO", self.Poveriteli[i][0])
            qs.setValue("TrustNo",self.Poveriteli[i][1])
        qs.endArray()

        size = qs.beginWriteArray("PModeli")
        c = len(self.PModeli)
        for i in range(c):
            qs.setArrayIndex(i)
            qs.setValue("FIO", self.PModeli[i])
        qs.endArray()

        size = qs.beginWriteArray("PMI")
        c = len(self.PMI)
        for i in range(c):
            qs.setArrayIndex(i)
            qs.setValue("MI", self.PMI[i][0])
            qs.setValue("string1",self.PMI[i][1])
            qs.setValue("string2",self.PMI[i][2])
            qs.setValue("string3",self.PMI[i][3])
        qs.endArray()

        size = qs.beginWriteArray("tModeli")
        c = len(self.tModeli)
        for i in range(c):
            qs.setArrayIndex(i)
            qs.setValue("FIO", self.tModeli[i])
        qs.endArray()
