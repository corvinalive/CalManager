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
	
	connect(AddButton, SIGNAL(clicked(bool)), this, SLOT(add_button_clicked(bool)));	connect(DeleteButton, SIGNAL(clicked(bool)), this, SLOT(delete_button_clicked(bool)));	connect(buttonBox, SIGNAL(accepted()), this, SLOT(ok_button_clicked()));
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
}
//-----------------------------------------------------------------------------
void QOptionsDialog::delete_button_clicked (bool)
{
	int i = CompanyTableWidget->currentRow();
	CompanyTableWidget->removeRow(i);
}
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
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------


