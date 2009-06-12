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
#include "qtempwidget.h"
#include <QLabel>
#include <QFile>
#include <QMessageBox>
#include <QProcess>

//-----------------------------------------------------------------------------
QTempWidget::QTempWidget(QWidget *parent)
 : QWidget(parent)
{
	setupUi(this);
	SetupControls();
	
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
	Calculate();
}
//-----------------------------------------------------------------------------
QTempWidget::~QTempWidget()
{
}
//-----------------------------------------------------------------------------
/*!
    \fn QTempWidget::SetupControls()
 */
void QTempWidget::SetupControls(bool )
{
    /// @todo implement me
	//read min % max
	min=minBox->value();
	max=maxBox->value();
	
	pmin=pminBox->value();
	pmax=pmaxBox->value();
	
	//set current date
	dateEdit->setDate(QDate::currentDate());
	
	double vv=16;

	//fill temp values
	t[0]=pmin;
	p1Value->setText(QString("%1").arg(pmin, 0, 'f', 3));
	t1->setValue(pmin);
	
	double cur=(pmax-pmin)/5+pmin;
	t[1]=cur;
	p2Value->setText(QString("%1").arg(cur, 0, 'f', 3));
	t2->setValue(cur);

	cur=2*(pmax-pmin)/5+pmin;
	t[2]=cur;
	p3Value->setText(QString("%1").arg(cur, 0, 'f', 3));
	t3->setValue(cur);
	
	cur=3*(pmax-pmin)/5+pmin;
	t[3]=cur;
	p4Value->setText(QString("%1").arg(cur, 0, 'f', 3));
	t4->setValue(cur);
	
	cur=4*(pmax-pmin)/5+pmin;
	t[4]=cur;
	p5Value->setText(QString("%1").arg(cur, 0, 'f', 3));
	t5->setValue(cur);

	cur=pmax;
	t[5]=cur;
	p6Value->setText(QString("%1").arg(cur, 0, 'f', 3));
	t6->setValue(cur);
	
	//fil i values
	double x=pmin;
	double i=(x-min)/(max-min);
	i=i*16+4;
	i1->setValue(i);
	
	x=(pmax-pmin)/5+pmin;
	i=(x-min)/(max-min);
	i=i*16+4;
	i2->setValue(i);

	x=2*(pmax-pmin)/5+pmin;
	i=(x-min)/(max-min);
	i=i*16+4;
	i3->setValue(i);

	x=3*(pmax-pmin)/5+pmin;
	i=(x-min)/(max-min);
	i=i*16+4;
	i4->setValue(i);

	x=4*(pmax-pmin)/5+pmin;
	i=(x-min)/(max-min);
	i=i*16+4;
	i5->setValue(i);

	x=pmax;
	i=(x-min)/(max-min);
	i=i*16+4;
	i6->setValue(i);

	Calculate();

}
//-----------------------------------------------------------------------------
/*!
    \fn QTempWidget::Calculate()
 */
void QTempWidget::Calculate()
{
	i[0]=i1->value();
	td[0]=t1->value();
	ti[0]=(i[0]-4)/16*(max-min)+min;
	d[0]=ti[0]-td[0];
	i1Value->setText(QString("%1").arg(ti[0], 0, 'f', 2));
	du1->setText(QString("%1").arg(d[0], 0, 'f', 2));
	
	i[1]=i2->value();
	td[1]=t2->value();
	ti[1]=(i[1]-4)/16*(max-min)+min;
	d[1]=ti[1]-td[1];
	i2Value->setText(QString("%1").arg(ti[1], 0, 'f', 2));
	du2->setText(QString("%1").arg(d[1], 0, 'f', 2));
	
	i[2]=i3->value();
	td[2]=t3->value();
	ti[2]=(i[2]-4)/16*(max-min)+min;
	d[2]=ti[2]-td[2];
	i3Value->setText(QString("%1").arg(ti[2], 0, 'f', 2));
	du3->setText(QString("%1").arg(d[2], 0, 'f', 2));
	
	i[3]=i4->value();
	td[3]=t4->value();
	ti[3]=(i[3]-4)/16*(max-min)+min;
	d[3]=ti[3]-td[3];
	i4Value->setText(QString("%1").arg(ti[3], 0, 'f', 2));
	du4->setText(QString("%1").arg(d[3], 0, 'f', 2));
	
	i[4]=i5->value();
	td[4]=t5->value();
	ti[4]=(i[4]-4)/16*(max-min)+min;
	d[4]=ti[4]-td[4];
	i5Value->setText(QString("%1").arg(ti[4], 0, 'f', 2));
	du5->setText(QString("%1").arg(d[4], 0, 'f', 2));
	
	i[5]=i6->value();
	td[5]=t6->value();
	ti[5]=(i[5]-4)/16*(max-min)+min;
	d[5]=ti[5]-td[5];
	i6Value->setText(QString("%1").arg(ti[5], 0, 'f', 2));
	du6->setText(QString("%1").arg(d[5], 0, 'f', 2));
	
}
//-----------------------------------------------------------------------------
void QTempWidget::ivalueChanged (double)
{
	Calculate();
}
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
void QTempWidget::rangevalueChanged (double)
{
	SetupControls();
	Calculate();
}
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
void QTempWidget::print_button_clicked (bool)
{
	Print();
}
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------


/*!
    \fn QTempWidget::Print()
 */
void QTempWidget::Print()
{
	//delete temp file
	QFile::remove("temperature.temp");
	
	//copy print.odt to print.temp
	if(!	QFile::copy("temperature.odt","temperature.temp"))
	{
		QMessageBox msgBox;
		msgBox.setInformativeText(QObject::trUtf8("Ошибка копирования файла <temperature.odt> во временный файл <temperature.temp>"));
		msgBox.setText(QObject::trUtf8("Ошибка при формировании свидетельства и протокола поверки"));
		msgBox.exec();
		return;
	}
	
	//delete content.xml		
	QFile::remove("content.xml");
	
	//извлечение content.xml из print.temp
	QStringList arguments;
	arguments << "temperature.temp" << "content.xml";

	QProcess *unZip = new QProcess(this);
	unZip->start("unzip", arguments);
	
	if(!unZip->waitForFinished (5000))
	{
		QMessageBox msgBox;
		msgBox.setInformativeText(QObject::trUtf8("Ошибка извлечения файла <content.xml> из файла <temperature.temp>"));
		msgBox.setText(QObject::trUtf8("Ошибка при формировании свидетельства и протокола поверки"));
		msgBox.exec();
		return;
	}
	
	if(unZip->exitCode()!=0)
	{
		QMessageBox msgBox;
		msgBox.setInformativeText(QObject::trUtf8("Ошибка извлечения файла <content.xml> из файла <temperature.temp>: unzip вернул ненулевой код выхода"));
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
	
	str.replace(QString("DAY"),ss);

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
	str.replace(QString("MONTH"),ss);

	str.replace(QString("IPTYPE"),NameBox->currentText());
	
	str.replace(QString("KLEIMO"),KleimoEdit->text());
	
	str.replace(QString("SNIP"), SerialEdit->text());

	str.replace(QString("SNTSP"), SerialEdit_2->text());
	
	str.replace(QString("OWNER"), OwnerBox->currentText());
	
	str.replace(QString("TVOS"), VosduhEdit->text());
	
	str.replace(QString("ATMPRESS"), AtmEdit->text());

	str.replace(QString("VLAGA"), WaterEdit->text());
	
	str.replace(QString("POVER"), PoverBox->currentText());
	
	ss="";
	ss.setNum(min);
	str.replace(QString("MIN"), ss);
	ss.setNum(max);
	str.replace(QString("MAX"), ss);
	
	ss=QString("%1").arg(r0box->value(), 0, 'f', 3);
	str.replace(QString("RNULL"), ss);
	
	ss=QString("%1").arg(r100box->value(), 0, 'f', 3);
	str.replace(QString("RSTO"), ss);
//FILL TABLE
	//file 1st column
	ss.setNum(t[0]);
	str.replace(QString("TABL11"),ss);
	
	ss.setNum(t[1]);
	str.replace(QString("TABL21"),ss);
	
	ss.setNum(t[2]);
	str.replace(QString("TABL31"),ss);

	ss.setNum(t[3]);
	str.replace(QString("TABL41"),ss);

	ss.setNum(t[4]);
	str.replace(QString("TABL51"),ss);

	ss.setNum(t[5]);
	str.replace(QString("TABL61"),ss);

//fill 2nd column
	ss=QString("%1").arg(td[0], 0, 'f', 2);
	str.replace(QString("TABL12"),ss);
	
	ss=QString("%1").arg(td[1], 0, 'f', 2);
	str.replace(QString("TABL22"),ss);
	
	ss=QString("%1").arg(td[2], 0, 'f', 2);
	str.replace(QString("TABL32"),ss);

	ss=QString("%1").arg(td[3], 0, 'f', 2);
	str.replace(QString("TABL42"),ss);

	ss=QString("%1").arg(td[4], 0, 'f', 2);
	str.replace(QString("TABL52"),ss);

	ss=QString("%1").arg(td[5], 0, 'f', 2);
	str.replace(QString("TABL62"),ss);
	
//fill 3th column
	ss=QString("%1").arg(i[0], 0, 'f', 3);
	str.replace(QString("TABL13"),ss);
	
	ss=QString("%1").arg(i[1], 0, 'f', 3);
	str.replace(QString("TABL23"),ss);
	
	ss=QString("%1").arg(i[2], 0, 'f', 3);
	str.replace(QString("TABL33"),ss);

	ss=QString("%1").arg(i[3], 0, 'f', 3);
	str.replace(QString("TABL43"),ss);

	ss=QString("%1").arg(i[4], 0, 'f', 3);
	str.replace(QString("TABL53"),ss);

	ss=QString("%1").arg(i[5], 0, 'f', 3);
	str.replace(QString("TABL63"),ss);
	
//fill 4th column
	ss=QString("%1").arg(ti[0], 0, 'f', 2);
	str.replace(QString("TABL14"),ss);
	
	ss=QString("%1").arg(ti[1], 0, 'f', 2);
	str.replace(QString("TABL24"),ss);
	
	ss=QString("%1").arg(ti[2], 0, 'f', 2);
	str.replace(QString("TABL34"),ss);

	ss=QString("%1").arg(ti[3], 0, 'f', 2);
	str.replace(QString("TABL44"),ss);

	ss=QString("%1").arg(ti[4], 0, 'f', 2);
	str.replace(QString("TABL54"),ss);

	ss=QString("%1").arg(ti[5], 0, 'f', 2);
	str.replace(QString("TABL64"),ss);
	
//fill last column
	ss=QString("%1").arg(d[0], 0, 'f', 2);
	str.replace(QString("TABL15"),ss);
	
	ss=QString("%1").arg(d[1], 0, 'f', 2);
	str.replace(QString("TABL25"),ss);
	
	ss=QString("%1").arg(d[2], 0, 'f', 2);
	str.replace(QString("TABL35"),ss);

	ss=QString("%1").arg(d[3], 0, 'f', 2);
	str.replace(QString("TABL45"),ss);

	ss=QString("%1").arg(d[4], 0, 'f', 2);
	str.replace(QString("TABL55"),ss);

	ss=QString("%1").arg(d[5], 0, 'f', 2);
	str.replace(QString("TABL65"),ss);

	
	file.resize(0);
	file.write(str.toUtf8 ());
	file.close();
	
	
	
	//обновление content.xml из print.temp
	arguments.clear();
	arguments << "temperature.temp" << "content.xml";

	unZip = new QProcess(this);
	unZip->start("zip", arguments);
	
	if(!unZip->waitForFinished (5000))
	{
		QMessageBox msgBox;
		msgBox.setInformativeText(QObject::trUtf8("Обновления файла <content.xml> в файле <temperature.temp>"));
		msgBox.setText(QObject::trUtf8("Ошибка при формировании свидетельства и протокола поверки"));
		msgBox.exec();
		return;
	}
	
	if(unZip->exitCode()!=0)
	{
		QMessageBox msgBox;
		msgBox.setInformativeText(QObject::trUtf8("Ошибка обновления <content.xml> в файле <temperature.temp>: zip вернул ненулевой код выхода"));
		msgBox.setText(QObject::trUtf8("Ошибка при формировании свидетельства и протокола поверки"));
		msgBox.exec();
		return;
	}
	delete unZip;

	ss=QObject::trUtf8("ДТ ");
	ss+=(QDateTime::currentDateTime ().toString("yyyy MM dd hh mm ss")+".odt");
	QFile::copy("temperature.temp",ss);	
	
	QMessageBox msgBox;
	msgBox.setText(QObject::trUtf8("Протокол успешно сформирован"));
	msgBox.exec();
	
}
