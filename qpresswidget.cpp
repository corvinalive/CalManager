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
#include "qpresswidget.h"
#include <QLabel>
#include <QFile>
#include <QMessageBox>
#include <QProcess>
#include <QDir>
#include <QTextStream>
#include <QSettings>

//-----------------------------------------------------------------------------
QPressWidget::QPressWidget(QWidget *parent)
 : QWidget(parent)
{
	kpa_changed=false;
	mm_changed=false;

	setupUi(this);
	SetupControls();
	
	connect(i1u, SIGNAL(valueChanged (double)), this, SLOT(ivalueChanged(double)));
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
	
	Calculate();
}
//-----------------------------------------------------------------------------
QPressWidget::~QPressWidget()
{
}
//-----------------------------------------------------------------------------
/*!
    \fn QPressWidget::SetupControls()
 */
struct Company{
		QString Name;
		QString INN;
	};

void QPressWidget::SetupControls(bool )
{
    /// @todo implement me
	//Заполняем список компаний и их ИНН

	QSettings settings("calmanager.ini", QSettings::IniFormat);
	
	OwnerBox->clear();
	OwnerBox->addItem("");
		
	int size = settings.beginReadArray("companies");
	QString name;
	QString inn;
	QByteArray ba1,ba2;
	for (int i = 0; i < size; ++i) {
		settings.setArrayIndex(i);
		ba1 = settings.value("Name").toByteArray();
		ba2 = settings.value("INN").toByteArray();
		name=QString::fromLocal8Bit(ba1.data());
		OwnerBox->addItem(name,inn);
	}
	settings.endArray();	
//	Заполняем список моделей датчиков и их методик поверки, межповерочный интвервал

	NameBox->clear();
	NameBox->addItem("");
		
/*	file.setFileName("press-list.txt");
	if (file.open(QIODevice::ReadOnly | QIODevice::Text))
	{
		QTextStream in(&file);
		while (!in.atEnd())
		{
			QString line = in.readLine();
			line.trimmed();
			//check the line
			if(line[0]=='#')
				continue;
			if(line.isEmpty())
				continue;
			int i=line.indexOf('\t');
			QString model;
			if(i==-1)
			{
				model=line;
				NameBox->addItem(model);
			}
			else
			{
				model=line;
				model.remove(i,100000);
				QString mi=line;
				//остались методики и интервал
				mi.remove(0,i+1);
				i=mi.indexOf('\t');
//				OwnerBox->addItem(name,inn);
			}
			
		}
	}*/
	
	//read min % max
	min=minBox->value();
	max=maxBox->value();
	col_points=col_pointsBox->value();
	//set current date
	dateEdit->setDate(QDate::currentDate());
	
	double vv=16;

	//fill pressure values
	p1Value->setText(QString("%1").arg(min, 0, 'f', 3));
	
	double v=(max-min)/(col_points-1)+min;
	p2Value->setText(QString("%1").arg(v, 0, 'f', 3));
	
	v=2*(max-min)/(col_points-1)+min;
	p3Value->setText(QString("%1").arg(v, 0, 'f', 3));

	v=3*(max-min)/(col_points-1)+min;
	p4Value->setText(QString("%1").arg(v, 0, 'f', 3));
	
	if (col_points==5)
	{
		p5Value->setText(QString("%1").arg(max, 0, 'f', 3));
		p6Value->setText("");
	}
	else
	{
		v=4*(max-min)/(col_points-1)+min;
		p5Value->setText(QString("%1").arg(v, 0, 'f', 3));
		
		p6Value->setText(QString("%1").arg(max, 0, 'f', 3));
	}
	
	//fil i values
	//if(SetI==true)
	{
		v=4;
		i1Value->setText(QString("%1").arg(v, 0, 'f', 3));
	
		v=vv/(col_points-1)+4;
		i2Value->setText(QString("%1").arg(v, 0, 'f', 3));
	
		v=2*vv/(col_points-1)+4;
		i3Value->setText(QString("%1").arg(v, 0, 'f', 3));

		v=3*vv/(col_points-1)+4;
		i4Value->setText(QString("%1").arg(v, 0, 'f', 3));
	
		if (col_points==5)
		{
			v=20;
			i5Value->setText(QString("%1").arg(v, 0, 'f', 3));
			i6Value->setText("");
		}
		else
		{
			v=4*vv/(col_points-1)+4;
			i5Value->setText(QString("%1").arg(v, 0, 'f', 3));
		
			v=20;
			i6Value->setText(QString("%1").arg(v, 0, 'f', 3));
		}
	}
	
	//fill i inputs
	i1u->setValue(4);
	i1d->setValue(4);
	
	v=vv/(col_points-1)+4;
	i2u->setValue(v);
	i2d->setValue(v);
	
	v=(2*vv)/(col_points-1)+4;
	i3u->setValue(v);
	i3d->setValue(v);
	
	v=(3*vv)/(col_points-1)+4;
	i4u->setValue(v);
	i4d->setValue(v);
	
	if (col_points==5)
	{
		v=20;
		i5u->setValue(v);
		i5d->setValue(v);
		
		i6u->hide();
		i6d->hide();
	}
	else
	{
		v=(4*vv)/(col_points-1)+4;
		i5u->setValue(v);
		i5d->setValue(v);
	
		v=20;
		i6u->show();
		i6d->show();
		i6u->setValue(v);
		i6d->setValue(v);		
	}
	
	
	Calculate();
	
}
//-----------------------------------------------------------------------------
/*!
    \fn QPressWidget::Calculate()
 */
void QPressWidget::Calculate()
{
    /// @todo implement me
	//set maxp, maxv
	double v16=16;
	maxp=0;
	maxv=0;
	//set klass
	klass = KlassBox->value();
	//First point
	double v=4;
	double var;
	double i=i1u->value();
	double d=(i-v);
	double dp=d*100/v16;
	OutToLabel(du1,d,dp);
	if(dp<0)
		dp*=-1;
	if(dp>maxp)
		maxp=dp;
	
	var=i;
	
	i=i1d->value();
	d=(i-v);
	dp=d*100/v16;
	OutToLabel(dd1,d,dp);
	if(dp<0)
		dp*=-1;
	if(dp>maxp)
		maxp=dp;

	var-=i;
	if(var<0)
		var*=-1;
	OutToLabel(v1, var,(var*100/v16));
	if(var>maxv)
		maxv=var;
//2nd point
	v=(v16)/(col_points-1)+4;
	i=i2u->value();
	d=(i-v);
	dp=d*100/v16;
	OutToLabel(du2,d,dp);
	if(dp<0)
		dp*=-1;
	if(dp>maxp)
		maxp=dp;

	var=i;
	
	i=i2d->value();
	d=(i-v);
	dp=d*100/v16;
	OutToLabel(dd2,d,dp);
	if(dp<0)
		dp*=-1;
	if(dp>maxp)
		maxp=dp;

	var-=i;
	if(var<0)
		var*=-1;
	OutToLabel(v2, var,(var*100/v16));
	if(var>maxv)
		maxv=var;
	
	//3 point
	v=(2*v16)/(col_points-1)+4;
	i=i3u->value();
	d=(i-v);
	dp=d*100/v16;
	OutToLabel(du3,d,dp);
	if(dp<0)
		dp*=-1;
	if(dp>maxp)
		maxp=dp;

	var=i;
	
	i=i3d->value();
	d=(i-v);
	dp=d*100/v16;
	OutToLabel(dd3,d,dp);
	if(dp<0)
		dp*=-1;
	if(dp>maxp)
		maxp=dp;

	var-=i;
	if(var<0)
		var*=-1;
	OutToLabel(v3, var,(var*100/v16));
	if(var>maxv)
		maxv=var;

	//4 point
	v=(3*v16)/(col_points-1)+4;
	i=i4u->value();
	d=(i-v);
	dp=d*100/v16;
	OutToLabel(du4,d,dp);
	if(dp<0)
		dp*=-1;
	if(dp>maxp)
		maxp=dp;

	var=i;
	
	i=i4d->value();
	d=(i-v);
	dp=d*100/v16;
	OutToLabel(dd4,d,dp);
	if(dp<0)
		dp*=-1;
	if(dp>maxp)
		maxp=dp;

	var-=i;
	if(var<0)
		var*=-1;
	OutToLabel(v4, var,(var*100/v16));
	if(var>maxv)
		maxv=var;

	if (col_points==5)
	{
		v=20;
		i=i5u->value();
		d=(i-v);
		dp=d*100/v16;
		OutToLabel(du5,d,dp);
		if(dp<0)
			dp*=-1;
		if(dp>maxp)
			maxp=dp;
	
		var=i;
		
		i=i5d->value();
		d=(i-v);
		dp=d*100/v16;
		OutToLabel(dd5,d,dp);
		if(dp<0)
			dp*=-1;
		if(dp>maxp)
			maxp=dp;

		var-=i;
		if(var<0)
			var*=-1;
		OutToLabel(v5, var,(var*100/v16));
		if(var>maxv)
			maxv=var;
		
		du6->hide();
		dd6->hide();
		v6->hide();
	}
	else
	{
		v=(4*v16)/(col_points-1)+4;
		i=i5u->value();
		d=(i-v);
		dp=d*100/v16;
		OutToLabel(du5,d,dp);
		if(dp<0)
			dp*=-1;
		if(dp>maxp)
			maxp=dp;
	
		var=i;
		
		i=i5d->value();
		d=(i-v);
		dp=d*100/v16;
		OutToLabel(dd5,d,dp);
		if(dp<0)
			dp*=-1;
		if(dp>maxp)
			maxp=dp;

		var-=i;
		if(var<0)
			var*=-1;
		OutToLabel(v5, var,(var*100/v16));
		if(var>maxv)
			maxv=var;
		
		v=20;
		du6->show();
		dd6->show();
		i=i6u->value();
		d=(i-v);
		dp=d*100/v16;
		OutToLabel(du6,d,dp);
		if(dp<0)
			dp*=-1;
		if(dp>maxp)
			maxp=dp;
	
		var=i;
		
		i=i6d->value();
		d=(i-v);
		dp=d*100/v16;
		OutToLabel(dd6,d,dp);
		if(dp<0)
			dp*=-1;
		if(dp>maxp)
			maxp=dp;
		
		var-=i;
		if(var<0)
			var*=-1;
		v6->show();
		OutToLabel(v6, var,(var*100/v16));
		if(var>maxv)
			maxv=var;
	}
	maxv=maxv*100/v16;
	QString s=QString("%1%").arg(maxv, 0, 'f', 3);
	if(maxv > klass)
		label_maxv->setText(QString::fromLatin1("<font color=red>%1</font>").arg(s));	
	else
		label_maxv->setText(QString::fromLatin1("<font color=blue>%1</font>").arg(s));

	s=QString("%1%").arg(maxp, 0, 'f', 3);
	if(maxp > klass)
		label_maxd->setText(QString::fromLatin1("<font color=red>%1</font>").arg(s));	
	else
		label_maxd->setText(QString::fromLatin1("<font color=blue>%1</font>").arg(s));
}
//-----------------------------------------------------------------------------
void QPressWidget::ivalueChanged (double)
{
	Calculate();
}
//-----------------------------------------------------------------------------
/*!
    \fn QPressWidget::OutToLabel(QLabel* l,double d, double dp)
 */
void QPressWidget::OutToLabel(QLabel* l,double d, double dp)
{
    /// @todo implement me
	QString s=QString("%1 mA; %2%").arg(d, 0, 'f', 3).arg(dp,0,'f',3);
	if(dp<0)
		dp*=-1;
	if(dp > klass)
		l->setText(QString::fromLatin1("<font color=red>%1</font>").arg(s));	
	else
		l->setText(QString::fromLatin1("<font color=blue>%1</font>").arg(s));	
}
//-----------------------------------------------------------------------------
void QPressWidget::rangevalueChanged (double)
{
	//read min % max
	min=minBox->value();
	max=maxBox->value();
	//fill pressure values
	p1Value->setText(QString("%1").arg(min, 0, 'f', 3));
	
	double v=(max-min)/(col_points-1)+min;
	p2Value->setText(QString("%1").arg(v, 0, 'f', 3));
	
	v=2*(max-min)/(col_points-1)+min;
	p3Value->setText(QString("%1").arg(v, 0, 'f', 3));

	v=3*(max-min)/(col_points-1)+min;
	p4Value->setText(QString("%1").arg(v, 0, 'f', 3));
	
	if (col_points==5)
	{
		p5Value->setText(QString("%1").arg(max, 0, 'f', 3));
		p6Value->setText("");
	}
	else
	{
		v=4*(max-min)/(col_points-1)+min;
		p5Value->setText(QString("%1").arg(v, 0, 'f', 3));
		
		p6Value->setText(QString("%1").arg(max, 0, 'f', 3));
	}
	Calculate();
}
//-----------------------------------------------------------------------------
void QPressWidget::col_points_changed(int)
{
	SetupControls(true);
}
//-----------------------------------------------------------------------------
void QPressWidget::print_button_clicked (bool)
{
	Print();
}
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------


/*!
    \fn QPressWidget::Print()
 */
void QPressWidget::Print()
{
	//delete temp file
	QFile::remove("pressure.temp");
	
	//copy print.odt to print.temp
	if(!	QFile::copy("pressure.odt","pressure.temp"))
	{
		QMessageBox msgBox;
		msgBox.setInformativeText(QObject::trUtf8("Ошибка копирования файла <pressure.odt> во временный файл <pressure.temp>"));
		msgBox.setText(QObject::trUtf8("Ошибка при формировании свидетельства и протокола поверки"));
		msgBox.exec();
		return;
	}
	
	//delete content.xml		
	QFile::remove("content.xml");
	
	//извлечение content.xml из print.temp
	QStringList arguments;
	arguments << "pressure.temp" << "content.xml";

	QProcess *unZip = new QProcess(this);
	unZip->start("unzip", arguments);
	
	if(!unZip->waitForFinished (5000))
	{
		QMessageBox msgBox;
		msgBox.setInformativeText(QObject::trUtf8("Ошибка извлечения файла <content.xml> из файла <pressure.temp>"));
		msgBox.setText(QObject::trUtf8("Ошибка при формировании свидетельства и протокола поверки"));
		msgBox.exec();
		return;
	}
	
	if(unZip->exitCode()!=0)
	{
		QMessageBox msgBox;
		msgBox.setInformativeText(QObject::trUtf8("Ошибка извлечения файла <content.xml> из файла <pressure.temp>: unzip вернул ненулевой код выхода"));
		msgBox.setText(QObject::trUtf8("Ошибка при формировании свидетельства и протокола поверки"));
		msgBox.exec();
		return;
	}
	delete unZip;
		
	QFile file("content.xml");
	if (!file.open(QIODevice::ReadOnly | QIODevice::WriteOnly))
	{
		QMessageBox msgBox;
		msgBox.setInformativeText(QObject::trUtf8("Ошибка открытия файла <content.xml>"));
		msgBox.setText(QObject::trUtf8("Ошибка при формировании свидетельства и протокола поверки"));
		msgBox.exec();
		return;
	}
	
	QByteArray ba=file.readAll();
//	ФОРМИРОВАНИЕ ПРОТОКОЛА	
	QString ss;
	QString str=QString::fromUtf8(ba.data());

	if(DayBox->isChecked())
		ss=dateEdit->date().toString("dd");
	else
		//ss=QObject::trUtf8("");
		ss=QObject::trUtf8("<text:s text:c=\"4\"/>");
//	ss+= QString(10, ' ');
	
	str.replace(QString("d1s_y"),ss);

	if(MonthBox->isChecked())
	{
		int m=dateEdit->date().month();
		switch(m)
		{
			case 1:
				ss=QObject::trUtf8("января");
				break;
			case 2:
				ss=QObject::trUtf8("февраля");
				break;
			case 3:
				ss=QObject::trUtf8("марта");
				break;
			case 4:
				ss=QObject::trUtf8("апреля");
				break;
			case 5:
				ss=QObject::trUtf8("мая");
				break;
			case 6:
				ss=QObject::trUtf8("июня");
				break;
			case 7:
				ss=QObject::trUtf8("июля");
				break;
			case 8:
				ss=QObject::trUtf8("августа");
				break;
			case 9:
				ss=QObject::trUtf8("сентября");
				break;
			case 10:
				ss=QObject::trUtf8("октября");
				break;
			case 11:
				ss=QObject::trUtf8("ноября");
				break;
			case 12:
				ss=QObject::trUtf8("декабря");
				break;
		}//end switch
	}//end if
	else
		ss=QObject::trUtf8("<text:s text:c=\"20\"/>");
	str.replace(QString("month"),ss);

	//add year
	ss=dateEdit->date().toString("yyyy");
	str.replace(QString("ywhen"),ss);
	
	int yearbefore=dateEdit->date().year()+interval_box->value();
	ss.setNum(yearbefore);
	str.replace(QString("ybefore"), ss);	
	
	str.replace(QString("pribor"),NameBox->currentText());
	
	str.replace(QString("kleimo"),KleimoEdit->text());
	
	str.replace(QString("serial"), SerialEdit->text());

	str.replace(QString("owner"), OwnerBox->currentText());
	str.replace(QString("inn-inn-inn"), INNEdit->text());
	
//str.replace(QString("vosduh"), VosduhEdit->text());
	ss="";
	ss.setNum(tvos_box->value());
	str.replace(QString("vosduh"), ss);	
	
	ss.setNum(atmkpa_box->value());
	str.replace(QString("atm"), ss);

	ss.setNum(water_box->value());
	str.replace(QString("water"), ss);
	
	str.replace(QString("pover"), PoverBox->currentText());

	ss="";
	ss.setNum(klass);
	str.replace(QString("klass"), ss);

	str.replace(QString("unit"), UnitBox->currentText());
	
/*
	dy	day
	month
	name
	kleimo
	serial
	klass
	owner
	vosduh
	atm
	water
	pover	
	ma-xd
	m-axv
	
	tablX1 - значение поверяемой величины
	Х2	- расчетный ток
	Х3	-	прямой ход
	4	обратный ход
	5, 6 - погршеност
	7 - вариация
	*/
	

	ss.setNum(max);
	str.replace(QString("max"), ss);
	
	//FILL TABLE
	
	//file 1st column
	ss=QString("%1").arg(min, 0, 'f', 3);
	str.replace(QString("tabl11"),ss);
	
	double v=(max-min)/(col_points-1)+min;
	ss=QString("%1").arg(v, 0, 'f', 3);
	str.replace(QString("tabl21"),ss);
	
	v=2*(max-min)/(col_points-1)+min;
	ss=QString("%1").arg(v, 0, 'f', 3);
	str.replace(QString("tabl31"),ss);

	v=3*(max-min)/(col_points-1)+min;
	ss=QString("%1").arg(v, 0, 'f', 3);
	str.replace(QString("tabl41"),ss);

	
	if (col_points==5)
	{
		ss=QString("%1").arg(max, 0, 'f', 3);
		str.replace(QString("tabl51"),ss);

		ss="";
		str.replace(QString("tabl61"),ss);
	}
	else
	{
		v=4*(max-min)/(col_points-1)+min;
		ss=QString("%1").arg(v, 0, 'f', 3);
		str.replace(QString("tabl51"),ss);
		
		ss=QString("%1").arg(max, 0, 'f', 3);
		str.replace(QString("tabl61"),ss);
	}

	//fil 2nd column
	v=4;
	double vv=16;
	ss=(QString("%1").arg(v, 0, 'f', 3));
	str.replace(QString("tabl12"),ss);
	
	v=vv/(col_points-1)+4;
	ss=(QString("%1").arg(v, 0, 'f', 3));
	str.replace(QString("tabl22"),ss);
	
	v=2*vv/(col_points-1)+4;
	ss=(QString("%1").arg(v, 0, 'f', 3));
	str.replace(QString("tabl32"),ss);

	v=3*vv/(col_points-1)+4;
	ss=(QString("%1").arg(v, 0, 'f', 3));
	str.replace(QString("tabl42"),ss);
	
	if (col_points==5)
	{
		v=20;
		ss=(QString("%1").arg(v, 0, 'f', 3));
		str.replace(QString("tabl52"),ss);
		ss="";
		str.replace(QString("tabl62"),ss);
	}
	else
	{
		v=4*vv/(col_points-1)+4;
		ss=(QString("%1").arg(v, 0, 'f', 3));
		str.replace(QString("tabl52"),ss);
		
		v=20;
		ss=(QString("%1").arg(v, 0, 'f', 3));
		str.replace(QString("tabl62"),ss);
	}

	//прямой ход
	ss=(QString("%1").arg(i1u->value(), 0, 'f', 3));
	str.replace(QString("tabl13"),ss);
	
	ss=(QString("%1").arg(i2u->value(), 0, 'f', 3));
	str.replace(QString("tabl23"),ss);
	
	ss=(QString("%1").arg(i3u->value(), 0, 'f', 3));
	str.replace(QString("tabl33"),ss);
	
	ss=(QString("%1").arg(i4u->value(), 0, 'f', 3));
	str.replace(QString("tabl43"),ss);

	ss=(QString("%1").arg(i5u->value(), 0, 'f', 3));
	str.replace(QString("tabl53"),ss);

	if (col_points==5)
	{
		str.replace(QString("tabl63"),QString(""));
	}
	else
	{
		ss=(QString("%1").arg(i6u->value(), 0, 'f', 3));
		str.replace(QString("tabl63"),ss);
	}
	
	//обратный ход
	ss=(QString("%1").arg(i1d->value(), 0, 'f', 3));
	str.replace(QString("tabl14"),ss);
	
	ss=(QString("%1").arg(i2d->value(), 0, 'f', 3));
	str.replace(QString("tabl24"),ss);
	
	ss=(QString("%1").arg(i3d->value(), 0, 'f', 3));
	str.replace(QString("tabl34"),ss);
	
	ss=(QString("%1").arg(i4d->value(), 0, 'f', 3));
	str.replace(QString("tabl44"),ss);

	ss=(QString("%1").arg(i5d->value(), 0, 'f', 3));
	str.replace(QString("tabl54"),ss);

	if (col_points==5)
	{
		str.replace(QString("tabl64"),QString(""));
	}
	else
	{
		ss=(QString("%1").arg(i6d->value(), 0, 'f', 3));
		str.replace(QString("tabl64"),ss);
	}

	//погрешность прямой ход, мА
	//First point
	v=4;
	double v16=16;
	double var;
	double i=i1u->value();
	double d=(i-v);
	ss=(QString("%1").arg(d, 0, 'f', 3));
	str.replace(QString("tabl15"),ss);
	var=i;
	i=i1d->value();
	d=(i-v);
	ss=(QString("%1").arg(d, 0, 'f', 3));
	str.replace(QString("tabl16"),ss);
	var-=i;
	if(var<0)
		var*=-1;
	ss=(QString("%1").arg(var, 0, 'f', 3));
	str.replace(QString("tabl17"),ss);

	v=(v16)/(col_points-1)+4;
	i=i2u->value();
	d=(i-v);
	ss=(QString("%1").arg(d, 0, 'f', 3));
	str.replace(QString("tabl25"),ss);
	var=i;
	i=i2d->value();
	d=(i-v);
	ss=(QString("%1").arg(d, 0, 'f', 3));
	str.replace(QString("tabl26"),ss);
	var-=i;
	if(var<0)
		var*=-1;
	ss=(QString("%1").arg(var, 0, 'f', 3));
	str.replace(QString("tabl27"),ss);
	
	v=(2*v16)/(col_points-1)+4;
	i=i3u->value();
	d=(i-v);
	ss=(QString("%1").arg(d, 0, 'f', 3));
	str.replace(QString("tabl35"),ss);
	var=i;
	i=i3d->value();
	d=(i-v);
	ss=(QString("%1").arg(d, 0, 'f', 3));
	str.replace(QString("tabl36"),ss);
	var-=i;
	if(var<0)
		var*=-1;
	ss=(QString("%1").arg(var, 0, 'f', 3));
	str.replace(QString("tabl37"),ss);
	
	v=(3*v16)/(col_points-1)+4;
	i=i4u->value();
	d=(i-v);
	ss=(QString("%1").arg(d, 0, 'f', 3));
	str.replace(QString("tabl45"),ss);
	var=i;
	i=i4d->value();
	d=(i-v);
	ss=(QString("%1").arg(d, 0, 'f', 3));
	str.replace(QString("tabl46"),ss);
	var-=i;
	if(var<0)
		var*=-1;
	ss=(QString("%1").arg(var, 0, 'f', 3));
	str.replace(QString("tabl47"),ss);
	
	v=(4*v16)/(col_points-1)+4;
	i=i5u->value();
	d=(i-v);
	ss=(QString("%1").arg(d, 0, 'f', 3));
	str.replace(QString("tabl55"),ss);
	var=i;
	i=i5d->value();
	d=(i-v);
	ss=(QString("%1").arg(d, 0, 'f', 3));
	str.replace(QString("tabl56"),ss);
	var-=i;
	if(var<0)
		var*=-1;
	ss=(QString("%1").arg(var, 0, 'f', 3));
	str.replace(QString("tabl57"),ss);
	
	if (col_points==5)
	{
		str.replace(QString("tabl65"),QString(""));
		str.replace(QString("tabl66"),QString(""));
		str.replace(QString("tabl67"),QString(""));
	}
	else
	{
		v=20;
		i=i6u->value();
		d=(i-v);
		ss=(QString("%1").arg(d, 0, 'f', 3));
		str.replace(QString("tabl65"),ss);
		var=i;
		i=i6d->value();
		d=(i-v);
		ss=(QString("%1").arg(d, 0, 'f', 3));
		str.replace(QString("tabl66"),ss);
		var-=i;
		if(var<0)
			var*=-1;
		ss=(QString("%1").arg(var, 0, 'f', 3));
		str.replace(QString("tabl67"),ss);
	}
	
	ss=QString("%1").arg(maxp, 0, 'f', 3);
	str.replace(QString("ma-xd"),ss);
	
	ss=QString("%1").arg(maxv, 0, 'f', 3);
	str.replace(QString("m-axv"),ss);
	
	
	file.resize(0);
	file.write(str.toUtf8 ());
	file.close();
	
	
	
	//обновление content.xml из print.temp
	arguments.clear();
	arguments << "pressure.temp" << "content.xml";

	unZip = new QProcess(this);
	unZip->start("zip", arguments);
	
	if(!unZip->waitForFinished (5000))
	{
		QMessageBox msgBox;
		msgBox.setInformativeText(QObject::trUtf8("Обновления файла <content.xml> в файле <pressure.temp>"));
		msgBox.setText(QObject::trUtf8("Ошибка при формировании свидетельства и протокола поверки"));
		msgBox.exec();
		return;
	}
	
	if(unZip->exitCode()!=0)
	{
		QMessageBox msgBox;
		msgBox.setInformativeText(QObject::trUtf8("Ошибка обновления <content.xml> в файле <pressure.temp>: zip вернул ненулевой код выхода"));
		msgBox.setText(QObject::trUtf8("Ошибка при формировании свидетельства и протокола поверки"));
		msgBox.exec();
		return;
	}
	delete unZip;

	//create new directory
	QDir dir;
	bool DirOk=false;
	ss=(QDateTime::currentDateTime ().toString("yyyy MM dd"));
	QString ss1=dir.path();
	ss1+=QObject::trUtf8("/");
	ss1+=ss;
	QMessageBox msgBox;
	//if(dir.exists())
			
	DirOk=dir.mkpath(ss);
	
	if(DirOk)
	{
		ss1=ss+QObject::trUtf8("/ДД ");
		ss1+=(QDateTime::currentDateTime ().toString("hh mm ss")+".odt");
	}
	else
	{
		ss1=QObject::trUtf8("ДД ");
		ss1+=(QDateTime::currentDateTime ().toString("yyyy MM dd hh mm ss")+".odt");
	}
	QFile::copy("pressure.temp",ss1);	
	QFile::remove("pressure.temp");
	QFile::remove("content.xml");
	
	
	msgBox.setText(QObject::trUtf8("Протокол успешно сформирован"));
	msgBox.exec();
}
//-----------------------------------------------------------------------------
void QPressWidget::atmkpavalueChanged (double kpa)
{
	if(mm_changed)
	{
		mm_changed=false;
		return;
	}
	kpa_changed=true;
	atmmm_box->setValue(kpa*7.50064);
}
//-----------------------------------------------------------------------------
void QPressWidget::atmmmvalueChanged (double mm)
{
	if(kpa_changed)
	{
		kpa_changed=false;
		return;
	}
	double kpa=mm;
	kpa=kpa/7.50064;
	mm_changed=true;
	atmkpa_box->setValue(kpa);
}
//-----------------------------------------------------------------------------
void QPressWidget::ownercurrentIndexChanged ( int index )
{
	if(index>=0)
	{
		QVariant v=OwnerBox->itemData(index);
		INNEdit->setText(v.toString());
	}
}
//-----------------------------------------------------------------------------
