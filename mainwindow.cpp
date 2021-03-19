#include "mainwindow.h"
#include "ui_mainwindow.h"
#include<QFile>
#include<QTextStream>
#include<QMessageBox>
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    //read from file upon start
    QFile file("C:/Users/Brian/Documents/Spring2021/Classes/CSPC362/ShoppingList-CPSC362/data.txt");
    if(!file.open(QFile::ReadOnly | QFile::Text))
    {
        QMessageBox::warning(this, "Error", "Error - The file is not open!");
    }
    QTextStream in(&file);
    QString contents;

    while(!file.atEnd())
    {
        contents = file.readLine();
        ui->listWidget_shoppingList->addItem(contents);
    }

    file.close();
}

MainWindow::~MainWindow()
{
    delete ui;
}


//Adds an item to the list upon clicking
void MainWindow::on_pushButton_add_clicked()
{
    QString item = ui->lineEdit_itemName->text();
    QString itemQuantity = ui->lineEdit_itemQuantity->text();

    ui->listWidget_shoppingList->addItem(item + ", " + itemQuantity);

    ui->lineEdit_itemName->clear();
    ui->lineEdit_itemQuantity->clear();
}

//edits an entry
void MainWindow::on_pushButton_edit_clicked()
{
    int currentRow = ui->listWidget_shoppingList->currentRow();
    QString item = ui->lineEdit_itemName->text();
    QString itemQuantity = ui->lineEdit_itemQuantity->text();
    ui->listWidget_shoppingList->item(currentRow)->setText(item + ", " + itemQuantity);
}

//deletes an entry
void MainWindow::on_pushButton_delete_clicked()
{
    QListWidgetItem *currentItem = ui->listWidget_shoppingList->currentItem();
    delete ui->listWidget_shoppingList->currentItem();
}
//saves data to file
void MainWindow::on_pushButton_save_clicked()
{
    QFile file("C:/Users/Brian/Documents/Spring2021/Classes/CSPC362/ShoppingList-CPSC362/data.txt");
    if(!file.open(QFile::WriteOnly | QFile::Text))
    {
        QMessageBox::warning(this, "Title", "Error - The file is not open!");
    }
    QTextStream out(&file);
    QString contents;
    int listSize = ui->listWidget_shoppingList->count();
    for(int index = 0;index < listSize;index++)
    {
        contents = ui->listWidget_shoppingList->item(index)->text();
        out << contents << "\n";
        file.flush();
    }
    QMessageBox::information(this, "Success", "Save complete!");
    file.close();
}
