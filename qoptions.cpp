/***************************************************************************
 *   Copyright (C) 2009 by Зонов В. М.   *
 *   corvinalive@list.ru   *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/
#include "qoptions.h"

QOptionsDialog::QOptionsDialog(QWidget *parent)
	: QDialog(parent)
{
	Ui_OptionsDialog::setupUi(this);

	//setupUi(this);
	
/*	connect(i1u, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i1d, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i2u, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i2d, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i3u, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i3d, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i4u, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i4d, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i5u, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i5d, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i6u, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	connect(i6d, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
	
	connect(KlassBox, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));

	connect(maxBox, SIGNAL(valueChanged (double)), this, SLOT(rangevalueChanged(double)));
	connect(minBox, SIGNAL(valueChanged (double)), this, SLOT(rangevalueChanged(double)));
	
	connect(col_pointsBox, SIGNAL(valueChanged (int)), this, SLOT(col_points_changed(int)));

	connect(PrintButton, SIGNAL(clicked(bool)), this, SLOT(print_button_clicked(bool)));
	
	connect(atmkpa_box, SIGNAL(valueChanged (double)), this, SLOT(atmkpavalueChanged(double)));
	
	connect(atmmm_box, SIGNAL(valueChanged (double)), this, SLOT(atmmmvalueChanged(double)));
	
	connect(OwnerBox, SIGNAL(currentIndexChanged(int)),this, SLOT(ownercurrentIndexChanged(int)));
	*/
}
//-----------------------------------------------------------------------------
QOptionsDialog::~QOptionsDialog()
{
}
//-----------------------------------------------------------------------------
