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
import shutil, sys

import ftplib

def GetUpdateInfo():
    try:
        ftp = ftplib.FTP("ims-nv.ru")
        ftp.login()
    
        ftp.cwd("calmanager")
        ftp.retrlines('LIST')
        ftp.retrbinary("RETR press_templates/list", open("press_list", "w+").write)
        ftp.retrbinary("RETR temp_templates/list", open("temp_list", "w+").write)
        ftp.quit()
    except ftplib.all_errors, err:
        print "error connect ftp lib\n", err
        
def LoadFile(server, filename,dest_filename):
    try:
        ftp = ftplib.FTP(server)
        ftp.login()
    
        ftp.retrbinary("RETR "+filename, open(dest_filename, "w+").write)
        ftp.quit()
    except ftplib.all_errors, err:
        print err

def LoadFiles(server, filenames):
    print ""
    try:
        ftp = ftplib.FTP(server,timeout=10)
        ftp.login()
        for fn in filenames:
            ftp.retrbinary("RETR "+fn[0], open(fn[1], "w+").write)
        ftp.quit()
    except ftplib.all_errors, err:
        print ftplib.all_errors
        print str(err)

import socket

def f():
    try:
        socket.gethostbyaddr('www.yandex.ru')
    except socket.gaierror:
        return False
    return True
 
	
def main():
    print "main", sys.path
    
    
    return 0	
    

if __name__ == '__main__':
    main()
