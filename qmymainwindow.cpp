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
#include "qmymainwindow.h"
#include "qpresswidget.h"
#include "qtempwidget.h"
#include "qoptions.h"


#include <QLabel>
#include <QMdiArea>
#include <QToolBar>
#include <QToolButton>
#include <QAction>
#include <QMessageBox>

//-----------------------------------------------------------------------------
QMyMainWindow::QMyMainWindow():QMainWindow()
{
	MDIArea = new QMdiArea(this);
	MDIArea->setHorizontalScrollBarPolicy(Qt::ScrollBarAsNeeded);
	MDIArea->setVerticalScrollBarPolicy(Qt::ScrollBarAsNeeded);
	setCentralWidget(MDIArea);
	
	CreateActions();
	setWindowTitle(trUtf8("Поверка датчиков давления"));
}
//-----------------------------------------------------------------------------
QMyMainWindow::~QMyMainWindow()
{
}
//-----------------------------------------------------------------------------
void QMyMainWindow::PressButtonClicked()
{
	QPressWidget *pw=new QPressWidget(MDIArea);
	MDIArea->addSubWindow(pw);
	pw->show();
//	pw->move(40,40);
}
//-----------------------------------------------------------------------------
void QMyMainWindow::OptionsButtonClicked()
{
	QOptionsDialog *pw=new QOptionsDialog(this);
	//MDIArea->addSubWindow(pw);
	pw->show();
//	pw->move(40,40);
}
//-----------------------------------------------------------------------------
void QMyMainWindow::TempButtonClicked()
{
	QTempWidget *pw=new QTempWidget(MDIArea);
	MDIArea->addSubWindow(pw);
	pw->show();
//	pw->move(40,40);
}
//-----------------------------------------------------------------------------
void QMyMainWindow::CreateActions()
{
    /// @todo implement me
	QAction* newAct = new QAction(trUtf8("Давление"), this);
	newAct->setShortcut(trUtf8("Ctrl+N"));
	newAct->setStatusTip(trUtf8("Поверка датчика давления"));
	connect(newAct, SIGNAL(triggered()), this, SLOT(PressButtonClicked()));
	
	QAction* tAct = new QAction(trUtf8("Температура"), this);
	//newAct->setShortcut(trUtf8("Ctrl+N"));
	newAct->setStatusTip(trUtf8("Поверка датчика температуры"));
	connect(tAct, SIGNAL(triggered()), this, SLOT(TempButtonClicked()));
	
	QAction* optionsAct = new QAction(trUtf8("Настройки"), this);
	//aboutAct->setShortcut(tr("F1"));
	connect(optionsAct, SIGNAL(triggered()), this, SLOT(OptionsButtonClicked()));
	
	QAction* aboutAct = new QAction(trUtf8("О программе..."), this);
	aboutAct->setShortcut(tr("F1"));
	connect(aboutAct, SIGNAL(triggered()), this, SLOT(AboutButtonClicked()));
	
	QToolBar* fileToolBar = addToolBar(trUtf8("File"));
	fileToolBar->addAction(newAct);	
	fileToolBar->addAction(tAct);	
	fileToolBar->addAction(optionsAct);	
	fileToolBar->addAction(aboutAct);	
	
}
//-----------------------------------------------------------------------------
void QMyMainWindow::AboutButtonClicked()
{
	QMessageBox::about(this, trUtf8("Поверка датчиков давления и температуры"),
		trUtf8("Программа для обработки данных и формирования свидетельств и протоколов поверки датчиков давления и температуры.\n\nАвтор: Зонов В. М.\n\ne-mail: corvinalive@list.ru\n\nЛицензия: GPL v.2\n\nВерсия: 0.3"));
}
//-----------------------------------------------------------------------------
