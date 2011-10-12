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

import struct, sys, os
from PySide import QtCore, QtGui
import commondata, odt_tools

from pressure import Ui_PressForm

class PressForm(QtGui.QWidget):
    def __init__(self,cd,parent=None):
        super(PressForm, self).__init__(parent)
        self.ui = Ui_PressForm()
        self.ui.setupUi(self)
        self.Commondata = cd
        
        self.kpa_changed=False
        self.mm_changed=False
        
        self.SetupControls(First=True)
        
        self.connect(self.ui.i1u, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i1d, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i2u, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i2d, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i3u, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i3d, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i4u, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i4d, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i5u, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i5d, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i6u, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.i6d, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
        self.connect(self.ui.KlassBox, QtCore.SIGNAL("valueChanged(double)"), self.ivalueChanged)
                
        self.connect(self.ui.maxBox, QtCore.SIGNAL("valueChanged (double)"),self.rangevalueChanged)
        self.connect(self.ui.minBox, QtCore.SIGNAL("valueChanged (double)"),self.rangevalueChanged)
        self.connect(self.ui.col_pointsBox, QtCore.SIGNAL("valueChanged (int)"),self.rangevalueChanged)

        self.connect(self.ui.PrintButton, QtCore.SIGNAL("clicked(bool)"), self.print_button_clicked)	
        self.connect(self.ui.atmkpa_box, QtCore.SIGNAL("valueChanged (double)"),self.atmkpavalueChanged)
        self.connect(self.ui.atmmm_box, QtCore.SIGNAL("valueChanged (double)"),self.atmmmvalueChanged)
        self.connect(self.ui.OwnerBox, QtCore.SIGNAL("currentIndexChanged(int)"),self.ownercurrentIndexChanged)

    def SetupControls(self, First = False):
        self.min = self.ui.minBox.value()
        self.max = self.ui.maxBox.value()
        
        #set current date
        if First:
            self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
            
        if First:
            self.ui.OwnerBox.clear()
            self.ui.OwnerBox.addItem("")
            for i in self.Commondata.Companies:
                self.ui.OwnerBox.addItem(i[0],i[1])

            self.ui.NameBox.clear()
            self.ui.NameBox.addItem("")
            for i in self.Commondata.PModeli:
                self.ui.NameBox.addItem(i)
                
            #Заполняем список PoverBox
            self.ui.PoverBox.clear()
            self.ui.PoverBox.addItem("")
            for i in self.Commondata.Poveriteli:
                self.ui.PoverBox.addItem(i)
                
        self.col_points=self.ui.col_pointsBox.value()
        vv=16.0
        #fill pressure values
        self.ui.p1Value.setText("%.3f"%self.min)
        
        v=(self.max-self.min)/(self.col_points-1)+self.min
        self.ui.p2Value.setText("%.3f"%v)
        
        v=2*(self.max-self.min)/(self.col_points-1)+self.min
        self.ui.p3Value.setText("%.3f"%v)
        
        v=3*(self.max-self.min)/(self.col_points-1)+self.min
        self.ui.p4Value.setText("%.3f"%v)
        
        if self.col_points==5:
            self.ui.p5Value.setText("%.3f"%self.max)
            self.ui.p6Value.setText("")
        else:
            v=4*(self.max-self.min)/(self.col_points-1)+self.min
            self.ui.p5Value.setText("%.3f"%v)
            self.ui.p6Value.setText("%.3f"%self.max)
        
        #fil i values
        v=4
        self.ui.i1Value.setText("%.3f"%v)
        v=vv/(self.col_points-1)+4
        self.ui.i2Value.setText("%.3f"%v)
        v=2*vv/(self.col_points-1)+4
        self.ui.i3Value.setText("%.3f"%v)
        v=3*vv/(self.col_points-1)+4
        self.ui.i4Value.setText("%.3f"%v)
        
        if self.col_points==5:
            v=20
            self.ui.i5Value.setText("%.3f"%v)
            self.ui.i6Value.setText("")
        else:
            v=4*vv/(self.col_points-1)+4
            self.ui.i5Value.setText("%.3f"%v)
            v=20
            self.ui.i6Value.setText("%.3f"%v)
        #fill i inputs
        self.ui.i1u.setValue(4)
        self.ui.i1d.setValue(4)
        v=vv/(self.col_points-1)+4
        self.ui.i2u.setValue(v)
        self.ui.i2d.setValue(v)
        v=(2*vv)/(self.col_points-1)+4
        self.ui.i3u.setValue(v)
        self.ui.i3d.setValue(v)
        v=(3*vv)/(self.col_points-1)+4
        self.ui.i4u.setValue(v)
        self.ui.i4d.setValue(v)
        
        if self.col_points==5:
            v=20
            self.ui.i5u.setValue(v)
            self.ui.i5d.setValue(v)
            self.ui.i6u.hide()
            self.ui.i6d.hide()
        else:
            v=(4*vv)/(self.col_points-1)+4
            self.ui.i5u.setValue(v)
            self.ui.i5d.setValue(v)
            v=20
            self.ui.i6u.show()
            self.ui.i6d.show()
            self.ui.i6u.setValue(v)
            self.ui.i6d.setValue(v)
        self.Calculate()

    def Calculate(self):
        #set self.maxp, self.maxv
        v16=16.0
        self.maxp=0.0
        self.maxv=0.0
        #set klass
        klass = self.ui.KlassBox.value()
        #First point
        v=4.0
        var=0.0
        i=self.ui.i1u.value()
        d=(i-v)
        dp=d*100/v16
        self.OutToLabel(self.ui.du1,d,dp)
        if dp<0:
            dp*=-1
        if dp>self.maxp:
            self.maxp=dp
        
        var=i
        i=self.ui.i1d.value()
        d=(i-v)
        dp=d*100/v16
        self.OutToLabel(self.ui.dd1,d,dp)
        if dp<0:
            dp*=-1
        if dp>self.maxp:
            self.maxp=dp
            
        var-=i
        if var<0:
            var*=-1
        self.OutToLabel(self.ui.v1, var,(var*100/v16))
        if var>self.maxv:
            self.maxv=var
        
        #2nd point
        v=(v16)/(self.col_points-1)+4
        i=self.ui.i2u.value()
        d=(i-v)
        dp=d*100/v16
        self.OutToLabel(self.ui.du2,d,dp)
        if (dp<0):
            dp*=-1
        if(dp>self.maxp):
            self.maxp=dp
        var=i
        i=self.ui.i2d.value()
        d=(i-v)
        dp=d*100/v16
        self.OutToLabel(self.ui.dd2,d,dp)
        if(dp<0):
            dp*=-1
        if(dp>self.maxp):
            self.maxp=dp
        var-=i
        if(var<0):
            var*=-1
        self.OutToLabel(self.ui.v2, var,(var*100/v16))
        if(var>self.maxv):
            self.maxv=var
        #3 point
        v=(2*v16)/(self.col_points-1)+4
        i=self.ui.i3u.value()
        d=(i-v)
        dp=d*100/v16
        self.OutToLabel(self.ui.du3,d,dp)
        if(dp<0):
            dp*=-1
        if(dp>self.maxp):
            self.maxp=dp
        var=i
        i=self.ui.i3d.value()
        d=(i-v)
        dp=d*100/v16
        self.OutToLabel(self.ui.dd3,d,dp)
        if(dp<0):
            dp*=-1
        if(dp>self.maxp):
            self.maxp=dp
        
        var-=i
        if(var<0):
            var*=-1
        self.OutToLabel(self.ui.v3, var,(var*100/v16))
        if(var>self.maxv):
            self.maxv=var
        #4 point
        v=(3*v16)/(self.col_points-1)+4
        i=self.ui.i4u.value()
        d=(i-v)
        dp=d*100/v16
        self.OutToLabel(self.ui.du4,d,dp)
        if(dp<0):
            dp*=-1
        if(dp>self.maxp):
            self.maxp=dp
        var=i
        i=self.ui.i4d.value()
        d=(i-v)
        dp=d*100/v16
        self.OutToLabel(self.ui.dd4,d,dp)
        if(dp<0):
            dp*=-1
        if(dp>self.maxp):
            self.maxp=dp
        var-=i
        if(var<0):
            var*=-1
        self.OutToLabel(self.ui.v4, var,(var*100/v16))
        if(var>self.maxv):
            self.maxv=var
        if (self.col_points==5):
            v=20
            i=self.ui.i5u.value()
            d=(i-v)
            dp=d*100/v16
            self.OutToLabel(self.ui.du5,d,dp)
            if(dp<0):
                dp*=-1
            if(dp>self.maxp):
                self.maxp=dp
            var=i
            i=self.ui.i5d.value()
            d=(i-v)
            dp=d*100/v16
            self.OutToLabel(self.ui.dd5,d,dp)
            if(dp<0):
                dp*=-1
            if(dp>self.maxp):
                self.maxp=dp
            var-=i
            if(var<0):
                var*=-1
            self.OutToLabel(self.ui.v5, var,(var*100/v16))
            if(var>self.maxv):
                self.maxv=var
            self.ui.du6.hide()
            self.ui.dd6.hide()
            self.ui.v6.hide()
        else:
            v=(4*v16)/(self.col_points-1)+4
            i=self.ui.i5u.value()
            d=(i-v)
            dp=d*100/v16
            self.OutToLabel(self.ui.du5,d,dp)
            if(dp<0):
                dp*=-1
            if(dp>self.maxp):
                self.maxp=dp
            var=i
            i=self.ui.i5d.value()
            d=(i-v)
            dp=d*100/v16
            self.OutToLabel(self.ui.dd5,d,dp)
            if(dp<0):
                dp*=-1
            if(dp>self.maxp):
                self.maxp=dp
            var-=i
            if(var<0):
                var*=-1
            self.OutToLabel(self.ui.v5, var,(var*100/v16))
            if(var>self.maxv):
                self.maxv=var
            v=20
            self.ui.du6.show()
            self.ui.dd6.show()
            i=self.ui.i6u.value()
            d=(i-v)
            dp=d*100/v16
            self.OutToLabel(self.ui.du6,d,dp)
            if(dp<0):
                dp*=-1
            if(dp>self.maxp):
                self.maxp=dp
            var=i
            i=self.ui.i6d.value()
            d=(i-v)
            dp=d*100/v16
            self.OutToLabel(self.ui.dd6,d,dp)
            if(dp<0):
                dp*=-1
            if(dp>self.maxp):
                self.maxp=dp
            var-=i
            if(var<0):
                var*=-1
            self.ui.v6.show()
            self.OutToLabel(self.ui.v6, var,(var*100/v16))
            if(var>self.maxv):
                self.maxv=var
        self.maxv=self.maxv*100/v16
        s="%.3f"%self.maxv+"%"
        if(self.maxv > klass):
            self.ui.label_maxv.setText("<font color=red>%s</font>"%s)	
        else:
            self.ui.label_maxv.setText("<font color=blue>%s</font>"%s)
        s="%.3f"%self.maxp+"%"
        if(self.maxp > klass):
            self.ui.label_maxd.setText("<font color=red>%s</font>"%s)	
        else:
            self.ui.label_maxd.setText("<font color=blue>%s</font>"%s)

    def ivalueChanged(self,value):
        self.Calculate()
            
    def rangevalueChanged(self, value):
        self.SetupControls()
                
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
            self.ui.INNEdit.setText(self.ui.OwnerBox.itemData(index))
            
    def print_button_clicked(self):
        print "Print"         
        
    def OutToLabel(self,l, d, dp):
       s="%.3f mA; "%d
       ss="%.3f"%dp
       s=s+ss+"%"
       if dp<0:
           dp*=-1
       
       if dp > self.ui.KlassBox.value():
           l.setText("<font color=red>%s</font>"%s)
       else:
            l.setText("<font color=blue>%s</font>"%s)	

          
            
    def print_button_clicked(self):
        print "Print"
        fileName = QtGui.QFileDialog.getOpenFileName(None,u"Открыть шаблон", u"./Шаблоны давление", u"Файл-шаблон (*.odt)")
        if os.path.exists(fileName[0])==False:
            return
        #Заполняем список для замены
        a = []
        if self.ui.DayBox.isChecked():
            ss=self.ui.dateEdit.date().toString("dd")
        else:
            ss=u"<text:s text:c=\"4\"/>"
        a.append((u"d1s_y",ss))
        if self.ui.MonthBox.isChecked():
            m=self.ui.dateEdit.date().month()
            months=[u"января",u"февраля",u"марта",u"апреля",u"мая",u"июня",
                    u"июля",u"августа",u"сентября",u"октября",u"ноября",
                    u"декабря"]
            ss=months[m-1]
        else:
            ss=u"<text:s text:c=\"20\"/>"
        a.append((u"month",ss))
        
        #add year
        ss=self.ui.dateEdit.date().toString("yyyy")
        a.append((u"ywhen",ss))
        
        ss=str(self.ui.dateEdit.date().year()+1)
        #ss.setNum(yearbefore);
        a.append((u"ybefore", ss))
        a.append((u"pribor",self.ui.NameBox.currentText()))
        a.append((u"kleimo",self.ui.KleimoEdit.text()))
        a.append((u"serial", self.ui.SerialEdit.text()))
        a.append((u"metodika", self.ui.MIBox.currentText()))
        a.append((u"owner", self.ui.OwnerBox.currentText()))
        a.append((u"vosduh", self.ui.tvos_box.text()))
        a.append((u"atm", self.ui.atmkpa_box.text()))
        a.append((u"inn-inn-inn", self.ui.INNEdit.text()))
        a.append((u"water", self.ui.water_box.text()))
        a.append((u"pover", self.ui.PoverBox.currentText()))
        a.append((u"klass", str(self.ui.KlassBox.value())))
        a.append((u"unit", self.ui.UnitBox.currentText()))
        
        
        ss = str(self.min)
        a.append((u"min", ss))
        ss =str(self.max)
        a.append((u"max", ss))
        
        #file 1st column
        ss="%.3f"%self.min
        a.append((u"tabl11",ss))
        
        v=(self.max-self.min)/(self.col_points-1)+self.min
        ss="%.3f"%v
        a.append((u"tabl21",ss))
        v=2*(self.max-self.min)/(self.col_points-1)+self.min
        ss="%.3f"%v
        a.append((u"tabl31",ss))
        v=3*(self.max-self.min)/(self.col_points-1)+self.min
        ss="%.3f"%v
        a.append((u"tabl41",ss))
        if (self.col_points==5):
            ss="%.3f"%self.max
            a.append((u"tabl51",ss))
            ss=""
            a.append((u"tabl61",ss))
        else:
            v=4*(self.max-self.min)/(self.col_points-1)+self.min
            ss="%.3f"%v
            a.append((u"tabl51",ss))
            ss="%.3f"%self.max
            a.append((u"tabl61",ss))
            
        #fil 2nd column
        v=4
        vv=16
        ss="%.3f"%v
        a.append((u"tabl12",ss))
        v=vv/(self.col_points-1)+4
        ss="%.3f"%v
        a.append((u"tabl22",ss))
        
        v=2*vv/(self.col_points-1)+4
        ss="%.3f"%v
        a.append((u"tabl32",ss))
        v=3*vv/(self.col_points-1)+4
        ss="%.3f"%v
        a.append((u"tabl42",ss))
        if (self.col_points==5):
            v=20
            ss="%.3f"%v
            a.append((u"tabl52",ss))
            ss=""
            a.append((u"tabl62",ss))
        else:
            v=4*vv/(self.col_points-1)+4
            ss="%.3f"%v
            a.append((u"tabl52",ss))
            v=20
            ss="%.3f"%v
            a.append((u"tabl62",ss))
        #прямой ход
        ss="%.3f"%self.ui.i1u.value()
        a.append((u"tabl13",ss))
        ss="%.3f"%self.ui.i2u.value()
        a.append((u"tabl23",ss))
        ss="%.3f"%self.ui.i3u.value()
        a.append((u"tabl33",ss))
        ss="%.3f"%self.ui.i4u.value()
        a.append((u"tabl43",ss))
        ss="%.3f"%self.ui.i5u.value()
        a.append((u"tabl53",ss))
        if (self.col_points==5):
            a.append((u"tabl63",""))
        else:
            ss="%.3f"%self.ui.i6u.value()
            a.append((u"tabl63",ss))
        #обратный ход
        ss="%.3f"%self.ui.i1d.value()
        a.append((u"tabl14",ss))
        ss="%.3f"%self.ui.i2d.value()
        a.append((u"tabl24",ss))
        ss="%.3f"%self.ui.i3d.value()
        a.append((u"tabl34",ss))
        ss="%.3f"%self.ui.i4d.value()
        a.append((u"tabl44",ss))
        ss="%.3f"%self.ui.i5d.value()
        a.append((u"tabl54",ss))
        if (self.col_points==5):
            a.append((u"tabl64",""))
        else:
            ss="%.3f"%self.ui.i6d.value()
            a.append((u"tabl64",ss))
        #погрешность прямой ход, мА
        #First point
        v=4
        v16=16
        i=self.ui.i1u.value()
        d=(i-v)
        ss="%.3f"%d
        a.append((u"tabl15",ss))
        var=i
        i=self.ui.i1d.value()
        d=(i-v)
        ss="%.3f"%d
        a.append((u"tabl16",ss))
        var-=i
        if(var<0):
            var*=-1
        ss="%.3f"%var
        a.append((u"tabl17",ss))
        v=(v16)/(self.col_points-1)+4
        i=self.ui.i2u.value()
        d=(i-v)
        ss="%.3f"%d
        a.append((u"tabl25",ss))
        var=i
        i=self.ui.i2d.value()
        d=(i-v)
        ss="%.3f"%d
        a.append((u"tabl26",ss))
        var-=i
        if(var<0):
            var*=-1
        ss="%.3f"%var
        a.append((u"tabl27",ss))
        v=(2*v16)/(self.col_points-1)+4
        i=self.ui.i3u.value()
        d=(i-v)
        ss="%.3f"%d
        a.append((u"tabl35",ss))
        var=i
        i=self.ui.i3d.value()
        d=(i-v)
        ss="%.3f"%d
        a.append((u"tabl36",ss))
        var-=i
        if(var<0):
            var*=-1
        ss="%.3f"%var
        a.append((u"tabl37",ss))
        v=(3*v16)/(self.col_points-1)+4
        i=self.ui.i4u.value()
        d=(i-v)
        ss="%.3f"%d
        a.append((u"tabl45",ss))
        var=i
        i=self.ui.i4d.value()
        d=(i-v)
        ss="%.3f"%d
        a.append((u"tabl46",ss))
        var-=i
        if(var<0):
            var*=-1
        ss="%.3f"%var
        a.append((u"tabl47",ss))
        v=(4*v16)/(self.col_points-1)+4
        i=self.ui.i5u.value()
        d=(i-v)
        ss="%.3f"%d
        a.append((u"tabl55",ss))
        var=i
        i=self.ui.i5d.value()
        d=(i-v)
        ss="%.3f"%d
        a.append((u"tabl56",ss))
        var-=i
        if(var<0):
            var*=-1
        ss="%.3f"%var
        a.append((u"tabl57",ss))
        if (self.col_points==5):
            a.append((u"tabl65",""))
            a.append((u"tabl66",""))
            a.append((u"tabl67",""))
        else:
            v=20
            i=self.ui.i6u.value()
            d=(i-v)
            ss="%.3f"%d
            a.append((u"tabl65",ss))
            var=i
            i=self.ui.i6d.value()
            d=(i-v)
            ss="%.3f"%d
            a.append((u"tabl66",ss))
            var-=i
            if(var<0):
                var*=-1
            ss="%.3f"%var
            a.append((u"tabl67",ss))
        ss="%.3f"%self.maxp
        a.append((u"ma-xd",ss))
        ss="%.3f"%self.maxv
        a.append((u"m-axv",ss))

        odt_tools.Prepare_odt(fileName[0])
        odt_tools.Replace(a)
        odt_tools.Save_odt(fileName[0]+".temp")

