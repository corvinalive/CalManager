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

from temperature import Ui_TempForm

class TempForm(QtGui.QWidget):
    def __init__(self,parent=None):
        super(TempForm, self).__init__(parent)
        self.ui = Ui_TempForm()
        self.ui.setupUi(self)
"""
	connect(i1, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(t1, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i2, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(t2, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i3, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(t3, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i4, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(t4, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i5, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(t5, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i6, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(t6, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	
	connect(maxBox, SIGNAL(valueChanged (double)), this, SLOT(rangevalueChanged(double)));
	connect(minBox, SIGNAL(valueChanged (double)), this, SLOT(rangevalueChanged(double)));
	connect(pmaxBox, SIGNAL(valueChanged (double)), this, SLOT(rangevalueChanged(double)));
	connect(pminBox, SIGNAL(valueChanged (double)), this, SLOT(rangevalueChanged(double)));
	
	connect(PrintButton, SIGNAL(clicked(bool)), this, SLOT(print_button_clicked(bool)));
	
	kpa_changed=false;
	mm_changed=false;
	connect(atmkpa_box, SIGNAL(valueChanged (double)), this, SLOT(atmkpavalueChanged(double)));
	connect(atmmm_box, SIGNAL(valueChanged (double)), this, SLOT(atmmmvalueChanged(double)));
	connect(OwnerBox, SIGNAL(currentIndexChanged(int)),this, SLOT(ownercurrentIndexChanged(int)));
	
	Calculate();
"""

