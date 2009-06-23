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
#ifndef QMYMAINWINDOW_H
#define QMYMAINWINDOW_H

#include <QMainWindow>
#include "qoptions.h"

class QLabel;
class QMdiArea;

struct Company{
	QString Name;
	QString INN;
};
/**
	@author Зонов В. М. <corvinalive@list.ru>
*/
class QMyMainWindow : public QMainWindow
{
	Q_OBJECT
	QLabel* label;
	QOptionsDialog *OptionsDialog;
public:
	QMdiArea *MDIArea;
	
	
    QMyMainWindow();
	 ~QMyMainWindow();
    void CreateActions();
    void SaveSetting();
    void LoadSetting();
 	static QList<Company> Companies;
	static QStringList Poveriteli;
	static QStringList PModeli;
	static QStringList tModeli;
	 
	public slots:
		void PressButtonClicked();	 
		void AboutButtonClicked();	 
		void TempButtonClicked();	 
		void OptionsButtonClicked();	 
		void OptionsDialog_accepted();
};

#endif
