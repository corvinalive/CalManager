#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       temp_unit.py
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

import struct, sys
from PySide import QtCore, QtGui
import commondata

from temperature import Ui_TempForm

class TempForm(QtGui.QWidget):
    def __init__(self,cd,parent=None):
        super(TempForm, self).__init__(parent)
        self.ui = Ui_TempForm()
        self.ui.setupUi(self)
        self.Commondata = cd
        self.t = [1,2,3,4,5,6]
        self.ti = [1,2,3,4,5,6]
        self.i = [1,2,3,4,5,6]
        self.td = [1,2,3,4,5,6]
        self.d = [1,2,3,4,5,6]
        self.SetupControls()
        self.connect(self.ui.i1, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i2, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i3, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i4, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i5, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i6, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.t1, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.t2, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.t3, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.t4, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.t5, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.t6, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        
        self.connect(self.ui.maxBox, QtCore.SIGNAL("valueChanged (double)"),self.rangevalueChanged)
        self.connect(self.ui.minBox, QtCore.SIGNAL("valueChanged (double)"),self.rangevalueChanged)
        self.connect(self.ui.pmaxBox, QtCore.SIGNAL("valueChanged (double)"),self.rangevalueChanged)
        self.connect(self.ui.pminBox, QtCore.SIGNAL("valueChanged (double)"),self.rangevalueChanged)
        
        self.connect(self.ui.PrintButton, QtCore.SIGNAL("clicked(bool)"), self.print_button_clicked)
        
        self.kpa_changed=False
        self.mm_changed=False
        
        self.connect(self.ui.atmkpa_box, QtCore.SIGNAL("valueChanged (double)"),self.atmkpavalueChanged)
        self.connect(self.ui.atmmm_box, QtCore.SIGNAL("valueChanged (double)"),self.atmmmvalueChanged)
        self.connect(self.ui.OwnerBox, QtCore.SIGNAL("currentIndexChanged(int)"),self.ownercurrentIndexChanged)
	

    
    def SetupControls(self):
        self.min = self.ui.minBox.value()
        self.max = self.ui.maxBox.value()
        
        self.pmin = self.ui.pminBox.value()
        self.pmax= self.ui.pmaxBox.value()
        #set current date
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
        
        self.ui.OwnerBox.clear()
        self.ui.OwnerBox.addItem("")
        for i in self.Commondata.Companies:
            self.ui.OwnerBox.addItem(i[0],i[1])

        self.ui.NameBox.clear()
        self.ui.NameBox.addItem("")
        for i in self.Commondata.tModeli:
            self.ui.NameBox.addItem(i)
            
        #Заполняем список PoverBox
        self.ui.PoverBox.clear()
        self.ui.PoverBox.addItem("")
        for i in self.Commondata.Poveriteli:
            self.ui.PoverBox.addItem(i)
            
        vv=16
        #//fill temp values
        self.t[0]=self.pmin
        self.ui.p1Value.setText(("%.2f"%(self.pmin)))
        self.ui.t1.setValue(self.pmin)
        
        cur=(self.pmax-self.pmin)/5+self.pmin
        self.t[1]=cur
        self.ui.p2Value.setText(("%.2f"%(cur)))
        self.ui.t2.setValue(cur)
        
        cur=2*(self.pmax-self.pmin)/5+self.pmin
        self.t[2]=cur
        self.ui.p3Value.setText(("%.2f"%(cur)))
        self.ui.t3.setValue(cur)
        
        cur=3*(self.pmax-self.pmin)/5+self.pmin
        self.t[3]=cur
        self.ui.p4Value.setText(("%.2f"%(cur)))
        self.ui.t4.setValue(cur)
        
        cur=4*(self.pmax-self.pmin)/5+self.pmin
        self.t[4]=cur
        self.ui.p5Value.setText(("%.2f"%(cur)))
        self.ui.t5.setValue(cur)
        
        cur=self.pmax
        self.t[5]=cur
        self.ui.p6Value.setText(("%.2f"%(cur)))
        self.ui.t6.setValue(cur)
        
        #//fil i values
        x=self.pmin
        i=(x-self.min)/(self.max-self.min)
        i=i*16+4
        self.ui.i1.setValue(i)
        
        x=(self.pmax-self.pmin)/5+self.pmin
        i=(x-self.min)/(self.max-self.min)
        i=i*16+4
        self.ui.i2.setValue(i)
        
        x=2*(self.pmax-self.pmin)/5+self.pmin
        i=(x-self.min)/(self.max-self.min)
        i=i*16+4
        self.ui.i3.setValue(i)
        
        x=3*(self.pmax-self.pmin)/5+self.pmin
        i=(x-self.min)/(self.max-self.min)
        i=i*16+4
        self.ui.i4.setValue(i)
        
        x=4*(self.pmax-self.pmin)/5+self.pmin
        i=(x-self.min)/(self.max-self.min)
        i=i*16+4
        self.ui.i5.setValue(i)
        
        x=self.pmax
        i=(x-self.min)/(self.max-self.min)
        i=i*16+4
        self.ui.i6.setValue(i)
        
        self.Calculate()
        
    def Calculate(self):
        self.i[0]=self.ui.i1.value()
        self.td[0]=self.ui.t1.value()
        self.ti[0]=(self.i[0]-4)/16*(self.max-self.min)+self.min
        self.d[0]=self.ti[0]-self.td[0]
        self.ui.i1Value.setText("%.2f"%self.ti[0])
        self.ui.du1.setText("%.2f"%self.d[0])
        
        self.i[1]=self.ui.i2.value()
        self.td[1]=self.ui.t2.value()
        self.ti[1]=(self.i[1]-4)/16*(self.max-self.min)+self.min
        self.d[1]=self.ti[1]-self.td[1]
        self.ui.i2Value.setText("%.2f"%self.ti[1])
        self.ui.du2.setText("%.2f"%self.d[1])

        self.i[2]=self.ui.i3.value()
        self.td[2]=self.ui.t3.value()
        self.ti[2]=(self.i[2]-4)/16*(self.max-self.min)+self.min
        self.d[2]=self.ti[2]-self.td[2]
        self.ui.i3Value.setText("%.2f"%self.ti[2])
        self.ui.du3.setText("%.2f"%self.d[2])

        self.i[3]=self.ui.i4.value()
        self.td[3]=self.ui.t4.value()
        self.ti[3]=(self.i[3]-4)/16*(self.max-self.min)+self.min
        self.d[3]=self.ti[3]-self.td[3]
        self.ui.i4Value.setText("%.2f"%self.ti[3])
        self.ui.du4.setText("%.2f"%self.d[3])

        self.i[4]=self.ui.i5.value()
        self.td[4]=self.ui.t5.value()
        self.ti[4]=(self.i[4]-4)/16*(self.max-self.min)+self.min
        self.d[4]=self.ti[4]-self.td[4]
        self.ui.i5Value.setText("%.2f"%self.ti[4])
        self.ui.du5.setText("%.2f"%self.d[4])

        self.i[5]=self.ui.i6.value()
        self.td[5]=self.ui.t6.value()
        self.ti[5]=(self.i[5]-4)/16*(self.max-self.min)+self.min
        self.d[5]=self.ti[5]-self.td[5]
        self.ui.i6Value.setText("%.2f"%self.ti[5])
        self.ui.du6.setText("%.2f"%self.d[5])
        
    def ivalueChanged(self,value):
        self.Calculate()
        
    def rangevalueChanged(self, value):
        self.SetupControls()
        self.Calculate()
        
    def atmkpavalueChanged(self, kpa):
        if self.mm_changed:
            self.mm_changed=False
            return
        self.kpa_changed=True
        self.ui.atmmm_box.setValue(kpa*7.50064)
        
    def atmmmvalueChanged(self, mm):
        if self.kpa_changed:
            self.kpa_changed=False
            return
        kpa=mm
        kpa=kpa/7.50064
        self.mm_changed=True
        self.ui.atmkpa_box.setValue(kpa)
        
    def ownercurrentIndexChanged(self, index ):
        if index>=0:
            #QtCore.QVariant v=self.ui.OwnerBox.itemData(index)
            #self.ui.INNEdit.setText(v.toString())
            self.ui.INNEdit.setText(self.ui.OwnerBox.itemData(index))
            
    def print_button_clicked(self):
        print "Print"
