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
#ifndef QPRESSWIDGET_H
#define QPRESSWIDGET_H

#include <QWidget>

#include "ui_Press.h"
class QLabel;

//#include "qmymainwindow.h"
/**
Класс окна для ввода данных температуры

	@author Зонов В. М. <corvinalive@list.ru>
*/
class QPressWidget : public QWidget, private Ui::PressForm
{
Q_OBJECT
private:
	double min,max;
	int col_points;
	double klass;
	double maxp;	//максимальная погрешность
	double maxv;	//max вариация	
	QLabel* label;
	bool kpa_changed;
	bool mm_changed;

public:
    QPressWidget(QWidget *parent = 0);

    ~QPressWidget();
    void SetupControls(bool setI=true);
    void Calculate();
    void Print();
	 
	public slots:
	 void ivalueChanged (double);
	 void rangevalueChanged (double);
	 void col_points_changed(int);
	 void print_button_clicked (bool);
	 void atmkpavalueChanged(double);
	 void	atmmmvalueChanged(double);
	 void ownercurrentIndexChanged ( int index );
	private:
    void OutToLabel(QLabel* l,double d, double dp);
};

#endif
