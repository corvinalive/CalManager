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
import shutil

def Prepare_odt(filename):
    #delete temp file
    tempfilename=filename+".temp"
    QtCore.QFile.remove(tempfilename)
	
	#copy print.odt to print.temp
    if QtCore.QFile.copy(filename,tempfilename)==False:
        msgBox = QtGui.QMessageBox()
        msgBox.setInformativeText(u("Ошибка копирования файла "+filename+" во временный файл "+tempfilename))
        msgBox.setText(u"Ошибка при формировании свидетельства и протокола поверки")
        msgBox.exec_()
        return
	
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
        msgBox.setInformativeText(u("Ошибка извлечения файла <content.xml> из файла"+tempfilename))
        msgBox.setText(u"Ошибка при формировании свидетельства и протокола поверки")
        msgBox.exec_()
        return
	
    if (unZip.exitCode()<>0) :
        msgBox = QtGui.QMessageBox()
        msgBox.setInformativeText(u("Ошибка извлечения файла <content.xml> из файла "+tempfilename+": unzip вернул ненулевой код выхода"))
        msgBox.setText(u"Ошибка при формировании свидетельства и протокола поверки")
        msgBox.exec_()
        return

def Save_odt(tempfilename, newfilename=None):
    #обновление content.xml из print.temp
    arguments =[]
    arguments.append(tempfilename)
    arguments.append("content.xml")

    unZip = QtCore.QProcess()
    unZip.start("zip", arguments)
	
    if unZip.waitForFinished (5000)==False:
        msgBox = QtGui.QMessageBox()
        msgBox.setInformativeText(u("Ошибка обновления файла <content.xml> в файле "+tempfilename))
        msgBox.setText(u"Ошибка при формировании свидетельства и протокола поверки")
        msgBox.exec_()
        return
    
    if unZip.exitCode() <> 0 :
        msgBox = QtGui.QMessageBox()
        msgBox.setInformativeText(u("Ошибка обновления <content.xml> в файле "+tempfilename+": zip вернул ненулевой код выхода"))
        msgBox.setText(u"Ошибка при формировании свидетельства и протокола поверки")
        msgBox.exec_()
        return
    
    #create new directory
    dir1 = QtCore.QDir()
    DirOk=False
    ss=(QtCore.QDateTime.currentDateTime().toString(u"yyyy MM dd"))
    ss1=dir1.currentPath()
    #QMessageBox msgBox
    #if(dir.exists())
            
    DirOk=dir1.mkpath(ss)

    if DirOk :
        ss1=ss+u"/ДТ "
        ss1+=(QtCore.QDateTime.currentDateTime ().toString(u"hh mm ss")+u".odt")
    else:
        ss1=u"ДТ "
        ss1+=u(QtCore.QDateTime.currentDateTime ().toString(u"yyyy MM dd hh mm ss")+u".odt")
    print ss1
    #QtCore.QFile.copy(tempfilename,ss1)	
    shutil.copyfile(tempfilename,ss1)
    QtCore.QFile.remove(tempfilename)
    QtCore.QFile.remove("content.xml")
	    
def Replace(spisok):
    #Функция замены слов в odt-файле
    #Нач. условия: файл content.xml лежит в текущей директории;
    #Принимаемый параметр: кортеж из пар (что_менять, на_что_поменять)
    fl = open("content.xml",'rb')
    str1 = fl.readline()
    str2 = unicode(fl.readline(),"Utf8")
    #for str1 in strings:
    #    str1 = unicode(str1,"Utf8")
    #for str1 in strings:
    str2 = str2.replace(u"POVER",u"Зонов")
    fl.close
    fl=open("content.xml",'wb')
    fl.truncate(0)
    fl.write(str1.encode("UTF-8"))
    fl.write(str2.encode("UTF-8"))
    #print strings
    fl.close()
    """
    fl = QtCore.QFile("content.xml")
	if fl.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.WriteOnly))!=True:
        #QMessageBox msgBox;
        #msgBox.setInformativeText(QObject::trUtf8("Ошибка открытия файла <content.xml>"));
        #msgBox.setText(QObject::trUtf8("Ошибка при формировании свидетельства и протокола поверки"));
        #msgBox.exec();
        return
	

    ba=QtCore.QByteArray()
    ba=fl.readAll()
#	ФОРМИРОВАНИЕ ПРОТОКОЛА	
	QString ss;
	QString str=QString::fromUtf8(ba.data());

	if(DayBox->isChecked())
		ss=dateEdit->date().toString("dd");
	else
		//ss=QObject::trUtf8("");
		ss=QObject::trUtf8("<text:s text:c=\"4\"/>");
//	ss+= QString(10, ' ');
	
	str.replace(QString("DAY"),ss);

	if(MonthBox->isChecked())
	{
		int m=dateEdit->date().month();
		switch(m)
		{
			case 1:
				ss=QObject::trUtf8("января");
				break;
			case 2:
				ss=QObject::trUtf8("февраля");
				break;
			case 3:
				ss=QObject::trUtf8("марта");
				break;
			case 4:
				ss=QObject::trUtf8("апреля");
				break;
			case 5:
				ss=QObject::trUtf8("мая");
				break;
			case 6:
				ss=QObject::trUtf8("июня");
				break;
			case 7:
				ss=QObject::trUtf8("июля");
				break;
			case 8:
				ss=QObject::trUtf8("августа");
				break;
			case 9:
				ss=QObject::trUtf8("сентября");
				break;
			case 10:
				ss=QObject::trUtf8("октября");
				break;
			case 11:
				ss=QObject::trUtf8("ноября");
				break;
			case 12:
				ss=QObject::trUtf8("декабря");
				break;
		}//end switch
	}//end if
	else
		ss=QObject::trUtf8("<text:s text:c=\"20\"/>");
	str.replace(QString("MONTH"),ss);

	//add year
	ss=dateEdit->date().toString("yyyy");
	str.replace(QString("ywhen"),ss);
	
	int yearbefore=dateEdit->date().year()+1;
	ss.setNum(yearbefore);
	str.replace(QString("ybefore"), ss);	

	str.replace(QString("IPTYPE"),NameBox->currentText());
	
	str.replace(QString("KLEIMO"),KleimoEdit->text());
	
	str.replace(QString("SNIP"), SerialEdit->text());

	str.replace(QString("SNTSP"), SerialEdit_2->text());
	
	str.replace(QString("OWNER"), OwnerBox->currentText());
	
	str.replace(QString("TVOS"), tvos_box->text());
	
	str.replace(QString("ATMPRESS"), atmkpa_box->text());

	str.replace(QString("inn-inn-inn"), INNEdit->text());

	str.replace(QString("VLAGA"), water_box->text());
	
	str.replace(QString("POVER"), PoverBox->currentText());
	
	ss="";
	ss.setNum(min);
	str.replace(QString("MIN"), ss);
	ss.setNum(max);
	str.replace(QString("MAX"), ss);
	
	ss=QString("%1").arg(r0box->value(), 0, 'f', 3);
	str.replace(QString("RNULL"), ss);
	
	ss=QString("%1").arg(r100box->value(), 0, 'f', 3);
	str.replace(QString("RSTO"), ss);
//FILL TABLE
	//file 1st column
	ss.setNum(t[0]);
	str.replace(QString("TABL11"),ss);
	
	ss.setNum(t[1]);
	str.replace(QString("TABL21"),ss);
	
	ss.setNum(t[2]);
	str.replace(QString("TABL31"),ss);

	ss.setNum(t[3]);
	str.replace(QString("TABL41"),ss);

	ss.setNum(t[4]);
	str.replace(QString("TABL51"),ss);

	ss.setNum(t[5]);
	str.replace(QString("TABL61"),ss);

//fill 2nd column
	ss=QString("%1").arg(td[0], 0, 'f', 2);
	str.replace(QString("TABL12"),ss);
	
	ss=QString("%1").arg(td[1], 0, 'f', 2);
	str.replace(QString("TABL22"),ss);
	
	ss=QString("%1").arg(td[2], 0, 'f', 2);
	str.replace(QString("TABL32"),ss);

	ss=QString("%1").arg(td[3], 0, 'f', 2);
	str.replace(QString("TABL42"),ss);

	ss=QString("%1").arg(td[4], 0, 'f', 2);
	str.replace(QString("TABL52"),ss);

	ss=QString("%1").arg(td[5], 0, 'f', 2);
	str.replace(QString("TABL62"),ss);
	
//fill 3th column
	ss=QString("%1").arg(i[0], 0, 'f', 3);
	str.replace(QString("TABL13"),ss);
	
	ss=QString("%1").arg(i[1], 0, 'f', 3);
	str.replace(QString("TABL23"),ss);
	
	ss=QString("%1").arg(i[2], 0, 'f', 3);
	str.replace(QString("TABL33"),ss);

	ss=QString("%1").arg(i[3], 0, 'f', 3);
	str.replace(QString("TABL43"),ss);

	ss=QString("%1").arg(i[4], 0, 'f', 3);
	str.replace(QString("TABL53"),ss);

	ss=QString("%1").arg(i[5], 0, 'f', 3);
	str.replace(QString("TABL63"),ss);
	
//fill 4th column
	ss=QString("%1").arg(ti[0], 0, 'f', 2);
	str.replace(QString("TABL14"),ss);
	
	ss=QString("%1").arg(ti[1], 0, 'f', 2);
	str.replace(QString("TABL24"),ss);
	
	ss=QString("%1").arg(ti[2], 0, 'f', 2);
	str.replace(QString("TABL34"),ss);

	ss=QString("%1").arg(ti[3], 0, 'f', 2);
	str.replace(QString("TABL44"),ss);

	ss=QString("%1").arg(ti[4], 0, 'f', 2);
	str.replace(QString("TABL54"),ss);

	ss=QString("%1").arg(ti[5], 0, 'f', 2);
	str.replace(QString("TABL64"),ss);
	
//fill last column
	ss=QString("%1").arg(d[0], 0, 'f', 2);
	str.replace(QString("TABL15"),ss);
	
	ss=QString("%1").arg(d[1], 0, 'f', 2);
	str.replace(QString("TABL25"),ss);
	
	ss=QString("%1").arg(d[2], 0, 'f', 2);
	str.replace(QString("TABL35"),ss);

	ss=QString("%1").arg(d[3], 0, 'f', 2);
	str.replace(QString("TABL45"),ss);

	ss=QString("%1").arg(d[4], 0, 'f', 2);
	str.replace(QString("TABL55"),ss);

	ss=QString("%1").arg(d[5], 0, 'f', 2);
	str.replace(QString("TABL65"),ss);

	
	file.resize(0);
	file.write(str.toUtf8 ());
	file.close();
"""
def main():
    print "main"
    Prepare_odt("temperature.odt")
    Replace(1)
    Save_odt("temperature.odt.temp")
    return 0	
    

if __name__ == '__main__':
    main()
