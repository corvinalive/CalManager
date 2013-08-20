#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       odt_tools.py
#       
#       Copyright 2011 imshp <imshp@imshp>
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

from PySide import QtCore, QtGui
import shutil, sys, locale, time, shutil

def Prepare_odt(filename,logg=None):
    #delete temp file
    tempfilename=filename+".temp"
    QtCore.QFile.remove(tempfilename)
	
	#copy print.odt to print.temp
    if QtCore.QFile.copy(filename,tempfilename)==False:
        msgBox = QtGui.QMessageBox()
        msgBox.setInformativeText(u"Ошибка копирования файла "+filename+u" во временный файл "+tempfilename)
        msgBox.setText(u"Ошибка при формировании свидетельства и протокола поверки")
        msgBox.exec_()
        return False
	
	#delete content.xml		
    QtCore.QFile.remove("content.xml")
	
	#извлечение content.xml из print.temp
    arguments = []
    arguments.append(tempfilename)
    arguments.append("content.xml")

    unZip = QtCore.QProcess()
    unZip.start("unzip", arguments)
	
    if unZip.waitForFinished(5000)==False:
        msgBox = QtGui.QMessageBox()
        msgBox.setInformativeText(u"Ошибка извлечения файла <content.xml> из файла"+tempfilename)
        msgBox.setText(u"Ошибка при формировании свидетельства и протокола поверки")
        msgBox.exec_()
        return False
	
    if (unZip.exitCode()<>0) :
        msgBox = QtGui.QMessageBox()
        msgBox.setInformativeText(u"Ошибка извлечения файла <content.xml> из файла "+tempfilename+u": unzip вернул ненулевой код выхода")
        msgBox.setText(u"Ошибка при формировании свидетельства и протокола поверки")
        msgBox.exec_()
        return False
    return True

def Save_odt(tempfilename, newfilename=None, Prefix1=None, Postfix1=None,logg=None):
    #обновление content.xml из print.temp
    #print "Prefix1=",Prefix1 
    arguments =[]
    arguments.append(tempfilename)
    arguments.append("content.xml")

    unZip = QtCore.QProcess()
    unZip.start("zip", arguments)
	
    if unZip.waitForFinished (5000)==False:
        msgBox = QtGui.QMessageBox()
        msgBox.setInformativeText(u"Ошибка обновления файла <content.xml> в файле "+tempfilename)
        msgBox.setText(u"Ошибка при формировании свидетельства и протокола поверки")
        msgBox.exec_()
        return False
    
    if unZip.exitCode() <> 0 :
        msgBox = QtGui.QMessageBox()
        msgBox.setInformativeText(u"Ошибка обновления <content.xml> в файле "+tempfilename+": zip вернул ненулевой код выхода")
        msgBox.setText(u"Ошибка при формировании свидетельства и протокола поверки")
        msgBox.exec_()
        return False
    
    #create new directory
    dir1 = QtCore.QDir()
    apppath=sys.path[0].decode(locale.getpreferredencoding(),"utf-8")
    dir1.cd(apppath)
    DirOk=False
    new_dir=(QtCore.QDateTime.currentDateTime().toString(u"yyyy MM dd"))
    DirOk=dir1.mkpath(new_dir)

    if(DirOk == False):
        logg.error(u"Ошибка создания папки "+new_dir)
    

    if Prefix1==None:
        Prefix1=""
    else:
        Prefix1+=" "

    current_time_str = QtCore.QDateTime.currentDateTime ().toString(u"hh mm ss")
    if DirOk :
        filename=apppath+"/"+new_dir+"/"+Prefix1+current_time_str
    else:
        filename=apppath+"/"+Prefix+current_time_str
        
    if Postfix1:
        filename+=" "+Postfix1+u".odt"
    else:
        filename+=u".odt"

    logg.info(u"Имя файла с результатом: "+filename)
    logg.info(u"Имя временного файла: "+tempfilename)

    shutil.copy(tempfilename,filename)

    QtCore.QFile.remove("content.xml")
    QtCore.QFile.remove(tempfilename)
    return True
	    
def Replace(spisok,logg=None):
    #Функция замены слов в odt-файле
    #Нач. условия: файл content.xml лежит в текущей директории;
    #Принимаемый параметр: кортеж из пар (что_менять, на_что_поменять)
    fl = open("content.xml",'rb+')

    flstr = unicode((fl.read()),"Utf8")
    #Делаем замены
    for items in spisok:
        flstr = flstr.replace(items[0],items[1])
    fl.seek(0)
    fl.truncate(0)
    fl.write(flstr.encode("UTF-8"))
    fl.close()
    return True

def GenerateDocument(TemplateFileName, ReplaceList, Prefix, logg=None):
    logg.info(u"TemplateFileName="+TemplateFileName+u" Prefix="+Prefix)
    res_ok=False
    if (Prepare_odt(TemplateFileName,logg=logg)==True):
        if (Replace(ReplaceList,logg=logg)==True):
            if (Save_odt(TemplateFileName+".temp",Prefix1=Prefix,logg=logg)==True):
                return True
    return False

	
def main():
    print "main"
    Prepare_odt("temperature.odt")
    a =[]
    a.append((u"POVER",u"Поверитель О. П."))
    a.append((u"KLEIMO",u"Номер клейма"))
    Replace(a)
    Save_odt("temperature.odt.temp")
    return 0	
    

if __name__ == '__main__':
    main()
