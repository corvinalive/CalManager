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
#include "qmymainwindow.h"
#include <QSettings>
#include <QList>
#include <QMessageBox>

QOptionsDialog::QOptionsDialog(QWidget *parent)
	: QDialog(parent)
{
	Ui_OptionsDialog::setupUi(this);
	CompanyTableWidget->setColumnWidth(1,150);
	CompanyTableWidget->setColumnWidth(0,350);
	
	connect(AddButton, SIGNAL(clicked(bool)), this, SLOT(add_button_clicked(bool)));
	connect(DeleteButton, SIGNAL(clicked(bool)), this, SLOT(delete_button_clicked(bool)));
	
	connect(AddPovButton, SIGNAL(clicked(bool)), this, SLOT(pov_add_button_clicked(bool)));
	connect(DeletePovButton, SIGNAL(clicked(bool)), this, SLOT(pov_delete_button_clicked(bool)));	
	
	connect(PAddButton, SIGNAL(clicked(bool)), this, SLOT(p_add_button_clicked(bool)));
	connect(PDeleteButton, SIGNAL(clicked(bool)), this, SLOT(p_delete_button_clicked(bool)));	
	
	connect(tAddButton, SIGNAL(clicked(bool)), this, SLOT(t_add_button_clicked(bool)));
	connect(tDeleteButton, SIGNAL(clicked(bool)), this, SLOT(t_delete_button_clicked(bool)));	
	
	
	connect(buttonBox, SIGNAL(accepted()), this, SLOT(ok_button_clicked()));
}
//-----------------------------------------------------------------------------
QOptionsDialog::~QOptionsDialog()
{
}
//-----------------------------------------------------------------------------
void QOptionsDialog::add_button_clicked (bool)
{
	CompanyTableWidget->setRowCount(CompanyTableWidget->rowCount()+1);
}
//-----------------------------------------------------------------------------
void QOptionsDialog::ok_button_clicked ()
{
	//Save changes
	int c=CompanyTableWidget->rowCount();
	QMyMainWindow::Companies.clear();
 	for (int i = 0; i < c ; ++i)
		{
		Company comp;
		comp.Name=CompanyTableWidget->item(i,0)->text();
		comp.INN=CompanyTableWidget->item(i,1)->text();
		QMyMainWindow::Companies.append(comp);
		}
	//Запись списка поверителей
		c=PovTableWidget->rowCount();
		QMyMainWindow::Poveriteli.clear();
		for (int i = 0; i < c ; ++i)
		{
			QMyMainWindow::Poveriteli.append(PovTableWidget->item(i,0)->text());
		}

		
		//Запись списка PModeli
		c=PTableWidget->rowCount();
		QMyMainWindow::PModeli.clear();
		for (int i = 0; i < c ; ++i)
		{
			QMyMainWindow::PModeli.append(PTableWidget->item(i,0)->text());
		}

		
		//Запись списка tModeli
		c=tTableWidget->rowCount();
		QMyMainWindow::tModeli.clear();
		for (int i = 0; i < c ; ++i)
		{
			QMyMainWindow::tModeli.append(tTableWidget->item(i,0)->text());
		}
		
		
		options_accepted();
}
//-----------------------------------------------------------------------------
void QOptionsDialog::Prepare()
{
	CompanyTableWidget->setRowCount(QMyMainWindow::Companies.size());
	int c=QMyMainWindow::Companies.size();
 	for (int i = 0; i < c ; ++i)
		{
		if(CompanyTableWidget->item(i,0)!=0)
			CompanyTableWidget->item(i,0)->setText(QMyMainWindow::Companies.value(i).Name);
		else
			{
			QTableWidgetItem*  item=new QTableWidgetItem(QMyMainWindow::Companies.value(i).Name);
			CompanyTableWidget->setItem(i,0,item);
			}
		
		if(CompanyTableWidget->item(i,1)!=0)
			CompanyTableWidget->item(i,1)->setText(QMyMainWindow::Companies.value(i).INN);
		else
			{
			QTableWidgetItem*  item=new QTableWidgetItem(QMyMainWindow::Companies.value(i).INN);
			CompanyTableWidget->setItem(i,1,item);
			}
		}
	//Заполнение списка поверителй
	PovTableWidget->setRowCount(QMyMainWindow::Poveriteli.size());
	c=QMyMainWindow::Poveriteli.size();
	for (int i = 0; i < c ; ++i)
		{
			if(PovTableWidget->item(i,0)!=0)
				PovTableWidget->item(i,0)->setText(QMyMainWindow::Poveriteli.value(i));
			else
			{
				QTableWidgetItem*  item=new QTableWidgetItem(QMyMainWindow::Poveriteli.value(i));
				PovTableWidget->setItem(i,0,item);
			}
		}
		
		
	//Заполнение списка PModeli
		PTableWidget->setRowCount(QMyMainWindow::PModeli.size());
		c=QMyMainWindow::PModeli.size();
		for (int i = 0; i < c ; ++i)
		{
			if(PTableWidget->item(i,0)!=0)
				PTableWidget->item(i,0)->setText(QMyMainWindow::PModeli.value(i));
			else
			{
				QTableWidgetItem*  item=new QTableWidgetItem(QMyMainWindow::PModeli.value(i));
				PTableWidget->setItem(i,0,item);
			}
		}
				
		
			//Заполнение списка tModeli
		tTableWidget->setRowCount(QMyMainWindow::tModeli.size());
		c=QMyMainWindow::tModeli.size();
		for (int i = 0; i < c ; ++i)
		{
			if(tTableWidget->item(i,0)!=0)
				tTableWidget->item(i,0)->setText(QMyMainWindow::tModeli.value(i));
			else
			{
				QTableWidgetItem*  item=new QTableWidgetItem(QMyMainWindow::tModeli.value(i));
				tTableWidget->setItem(i,0,item);
			}
		}
		
		
		
}
//-----------------------------------------------------------------------------
void QOptionsDialog::delete_button_clicked (bool)
{
	int i = CompanyTableWidget->currentRow();
	CompanyTableWidget->removeRow(i);
}
//-----------------------------------------------------------------------------
void QOptionsDialog::pov_delete_button_clicked (bool)
{
	int i = PovTableWidget->currentRow();
	PovTableWidget->removeRow(i);
}
//-----------------------------------------------------------------------------
void QOptionsDialog::pov_add_button_clicked (bool)
{
	PovTableWidget->setRowCount(PovTableWidget->rowCount()+1);
}
//-----------------------------------------------------------------------------


void QOptionsDialog::p_delete_button_clicked (bool)
{
	int i = PTableWidget->currentRow();
	PTableWidget->removeRow(i);
}
//-----------------------------------------------------------------------------
void QOptionsDialog::p_add_button_clicked (bool)
{
	PTableWidget->setRowCount(PTableWidget->rowCount()+1);
}
//-----------------------------------------------------------------------------//-------------
void QOptionsDialog::t_delete_button_clicked (bool)
{
	int i = tTableWidget->currentRow();
	tTableWidget->removeRow(i);
}
//-----------------------------------------------------------------------------
void QOptionsDialog::t_add_button_clicked (bool)
{
	tTableWidget->setRowCount(tTableWidget->rowCount()+1);
}
//-----------------------------------------------------------------------------//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------


