from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb

from PyQt5.uic import loadUiType

ui,_ = loadUiType('library.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_ui_change()
        self.Handel_Buttons()

        self.showcategory()
        self.showauthor()
        self.showpublisher()

        self.ShowAllBooks()

        self.show_category_combo()
        self.show_author_combo()
        self.show_publisher_combo()
    
    def Handel_ui_change(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)
        
    def Handel_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_17.clicked.connect(self.Hiding_Themes)
        
        # menu
        self.pushButton.clicked.connect(self.Open_day_to_day_tab)
        self.pushButton_2.clicked.connect(self.Open_books_tab)
        self.pushButton_26.clicked.connect(self.Open_Users_tab)
        self.pushButton_30.clicked.connect(self.Open_Client_tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_tab)

        # add book
        self.pushButton_7.clicked.connect(self.Addnewbook)
        
        # search book
        self.pushButton_9.clicked.connect(self.searchbooks)

        # update book
        self.pushButton_8.clicked.connect(self.Editbooks)

        # delete book
        self.pushButton_10.clicked.connect(self.Deletebooks)
        ## delete selected book
        self.pushButton_3.clicked.connect(self.deleteSelected)
        
        #add category
        self.pushButton_14.clicked.connect(self.Addcategory)

        # add author
        self.pushButton_15.clicked.connect(self.AddAuthor)

        # add publisher
        self.pushButton_16.clicked.connect(self.Addpublisher)


    def Show_Themes(self):
        self.groupBox_3.show()

    def Hiding_Themes(self):
        self.groupBox_3.hide()
    
    ################################
    #########opening tabs###########

    def Open_day_to_day_tab(self):
        self.tabWidget.setCurrentIndex(0)
    def Open_books_tab(self):
        self.tabWidget.setCurrentIndex(1)
    def Open_Users_tab(self):
        self.tabWidget.setCurrentIndex(3)
    def Open_Settings_tab(self):
        self.tabWidget.setCurrentIndex(4)
    def Open_Client_tab(self):
        self.tabWidget.setCurrentIndex(2)
    
    #################################
    #############Books###############

    def ShowAllBooks(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()
        
        self.cur.execute('''SELECT book_name,book_description,book_code,book_category,book_author,book_publisher,book_price FROM book ''' )
        data = self.cur.fetchall()

        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

        self.db.close()


    def deleteSelected(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        indexes = self.tableWidget_5.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = index.row()
            row_ = row+1
        self.cur.execute('''DELETE FROM book WHERE id = %s''' ,[(row_)])
        self.db.commit()
        self.ShowAllBooks()



    def Addnewbook(self):
        
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        id = self.lineEdit_30.text()
        book_title = self.lineEdit_2.text()
        book_code = self.lineEdit_3.text()
        book_description = self.textEdit.toPlainText()
        book_category = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()
        book_publisher = self.comboBox_5.currentText()
        book_price = self.lineEdit_4.text()

        self.cur.execute('''
            INSERT INTO book(id,book_name,book_description,book_code,book_category,book_price,book_author,book_publisher)
            VALUES (%s ,%s , %s , %s , %s , %s , %s , %s)
        ''' ,(id,book_title , book_description , book_code , book_category , book_price , book_author , book_publisher,))

        self.db.commit()
        self.statusBar().showMessage('New Book Added')

        self.lineEdit_2.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_3.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_4.setText('')
        self.ShowAllBooks()


    def searchbooks(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()
        
        book_title = self.lineEdit_5.text()

        sql = ''' SELECT * FROM book WHERE book_name = %s'''
        self.cur.execute(sql , [(book_title)])
        try:
            data = self.cur.fetchone()

            self.lineEdit_8.setText(data[1])
            self.textEdit_2.setPlainText(data[2])
            self.lineEdit_7.setText(data[3])
            self.comboBox_7.setCurrentText(data[4])
            self.comboBox_8.setCurrentText(data[6])
            self.comboBox_6.setCurrentText(data[7])
            self.lineEdit_6.setText(str(data[5]))   
            self.lineEdit_39.setText(str(data[0]))   
            self.statusBar().showMessage('')
        except:
            self.statusBar().showMessage('BOOK NOT FOUND!!!')


    def Editbooks(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        id = self.lineEdit_39.text()
        book_title = self.lineEdit_8.text()
        book_code = self.lineEdit_7.text()
        book_description = self.textEdit_2.toPlainText()
        book_category = self.comboBox_7.currentText()
        book_author = self.comboBox_8.currentText()
        book_publisher = self.comboBox_6.currentText()
        book_price = self.lineEdit_6.text()

        search_book_title = self.lineEdit_5.text()
        self.cur.execute('''
            UPDATE book SET id=%s,book_name=%s ,book_description=%s ,book_code=%s ,book_category=%s ,book_author=%s ,book_publisher=%s ,book_price=%s WHERE book_name = %s            
        ''', (id,book_title,book_description,book_code,book_category,book_author,book_publisher , book_price , search_book_title))

        self.db.commit()
        self.statusBar().showMessage('Book Updated')

        self.lineEdit_39.setText('')
        self.lineEdit_8.setText('')
        self.textEdit_2.setPlainText('')
        self.lineEdit_7.setText('')
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.lineEdit_6.setText('')
        self.ShowAllBooks()

    def Deletebooks(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()
        
        book_title = self.lineEdit_5.text()

        sql = ''' DELETE FROM book WHERE book_name = %s'''
        self.cur.execute(sql , [(book_title)])

        self.db.commit()
        self.statusBar().showMessage('Book Deleted')

        self.lineEdit_8.setText('')
        self.textEdit_2.setPlainText('')
        self.lineEdit_7.setText('')
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.lineEdit_6.setText('')
        self.ShowAllBooks()



    #################################
    #############Users###############

    def Add_New_User(self):
        pass
    
    def login(self):
        pass

    def Edituser(self):
        pass

    ###################################
    #############Setting###############
    def Addcategory(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        category_name = self.lineEdit_19.text()

        self.cur.execute('''
            INSERT INTO category(category) VALUES(%s)
        ''',(category_name,))

        self.db.commit()
        self.statusBar().showMessage('New Category Added')
        self.showcategory()
    
    def showcategory(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT category from category''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column,item in enumerate(form):
                    self.tableWidget_2.setItem(row,column,QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)
                
                

    def AddAuthor(self): 
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        author_name = self.lineEdit_20.text()

        self.cur.execute('''
            INSERT INTO authors(author) VALUES(%s)
        ''',(author_name,))

        self.db.commit()
        self.statusBar().showMessage('New Author Added')
        self.showauthor()

    def showauthor(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)

        self.cur = self.db.cursor()

        book_title = self.lineEdit_8.text()
        book_description = self.textEdit_2.toPlainText()
        book_code = self.lineEdit_7.text()
        book_category = self.comboBox_7.currentText()
        book_author = self.comboBox_8.currentText()
        book_publisher = self.comboBox_6.currentText()
        book_price = self.lineEdit_6.text()


        search_book_title = self.lineEdit_5.text()

        self.cur.execute('''
            UPDATE book SET book_name=%s ,book_description=%s ,book_code=%s ,book_category=%s ,book_author=%s ,book_publisher=%s ,book_price=%s WHERE book_name = %s            
        ''', (book_title,book_description,book_code,book_category,book_author,book_publisher , book_price , search_book_title))

        self.db.commit()
        self.statusBar().showMessage('book updated')
        self.ShowAllBooks()

    def Addpublisher(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_21.text()

        self.cur.execute('''
            INSERT INTO publisher(publisher_name) VALUES(%s)
        ''',(publisher_name,))

        self.db.commit()
        self.statusBar().showMessage('New Publisher Added')

    def showpublisher(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT publisher_name from publisher''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column,item in enumerate(form):
                    self.tableWidget_4.setItem(row,column,QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)

    def show_category_combo(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()
        
        self.cur.execute(''' SELECT category FROM category ''')
        data = self.cur.fetchall()

        self.comboBox_3.clear()
        for category in data :
            self.comboBox_3.addItem(category[0])
            self.comboBox_7.addItem(category[0])



    def show_author_combo(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()
        
        self.cur.execute(''' SELECT author FROM authors ''')
        data = self.cur.fetchall()

        self.comboBox_4.clear()
        for author in data :
            self.comboBox_4.addItem(author[0])
            self.comboBox_8.addItem(author[0])


    def show_publisher_combo(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()
        
        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()

        self.comboBox_5.clear()
        for publisher in data :
            self.comboBox_5.addItem(publisher[0])
            self.comboBox_6.addItem(publisher[0])


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()

        