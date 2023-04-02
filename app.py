from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb
import datetime
from PyQt5.uic import loadUiType
# from xlrd import *
from xlsxwriter import *

ui,_ = loadUiType('library.ui')

login,_ = loadUiType('login.ui')

class Login(QWidget , login):
    def __init__(self):
        QWidget.__init__(self)
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_Login)

    def Handel_Login(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[1] and password == row[3]:
                # print('user match')
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.setText('Make Sure You Enterd Your Username And Password Correctly')



class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)
        self.setupUi(self)
        self.Handel_ui_change()
        self.Handel_Buttons()

        self.showcategory()
        self.ShowAllBooks()
        self.Show_All_Operations_Student()
        self.Show_All_Operations_Teacher()
        self.Book_Not_Issued_Teacher()
        self.Book_Not_Issued_Student()
        self.show_category_combo()
        self.show_issued_combo()
        self.show_book_combo()

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
        self.pushButton_4.clicked.connect(self.Open_Settings_tab)

        # add book
        self.pushButton_7.clicked.connect(self.Addnewbook)
        
        # search book
        self.pushButton_9.clicked.connect(self.searchbooks)

        ## update selected book
        self.pushButton_37.clicked.connect(self.updateSelected)
        # self.pushButton_40.clicked.connect(self.updateSelectedSearch)

        ## delete selected book
        self.pushButton_3.clicked.connect(self.deleteSelected)
        # self.pushButton_16.clicked.connect(self.deleteSelected)

        #add category
        self.pushButton_14.clicked.connect(self.Addcategory)

        # add operations student
        self.pushButton_6.clicked.connect(self.HandleOperationsStudent)
        # self.show_book_combo()
        
        # add operations teacher
        self.pushButton_44.clicked.connect(self.HandleOperationsTeacher)
        # self.show_book_combo()

        #add user
        self.pushButton_11.clicked.connect(self.Add_New_User)

        #login
        self.pushButton_12.clicked.connect(self.login)

        #edit user data
        self.pushButton_13.clicked.connect(self.Edituser)

        # export books
        self.pushButton_27.clicked.connect(self.Export_Books)
        
        # export operations
        self.pushButton_29.clicked.connect(self.Export_Day_Operation_Student)
        self.pushButton_47.clicked.connect(self.Export_Day_Operation_Student_Returned)
        self.pushButton_45.clicked.connect(self.Export_Day_Operation_Teacher)
        self.pushButton_46.clicked.connect(self.Export_Day_Operation_Teacher_Returned)

        # Themes
        self.pushButton_19.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_18.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_21.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton_20.clicked.connect(self.QDark_Theme)

        # update operation
        self.pushButton_30.clicked.connect(self.updateOperation_Student)
        self.pushButton_31.clicked.connect(self.updateOperation_Teacher)



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
        self.tabWidget.setCurrentIndex(2)
    def Open_Settings_tab(self):
        self.tabWidget.setCurrentIndex(3)

    
    ######################################
    #############Operations###############

    def Show_All_Operations_Student(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT book_name , student_name , student_class , book_issued, date , date_to FROM dayoperations_student
        ''')

        data = self.cur.fetchall()

        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
        # self.show_book_combo()

    def Show_All_Operations_Teacher(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT book_name , teacher_name , teacher_subject , book_issued ,date , date_to FROM dayoperations_teacher
        ''')

        data = self.cur.fetchall()

        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget_3.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_position)
        # self.show_book_combo()

        
    def HandleOperationsStudent(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        book_title = self.comboBox.currentText()
        student_name = self.lineEdit_29.text()
        student_class = self.lineEdit_57.text()
        days = self.comboBox_2.currentIndex() + 1
        today_date = datetime.date.today()
        to_date = today_date + datetime.timedelta(days=days)


        self.cur.execute('''
            INSERT INTO dayoperations_student(book_name,student_name,student_class,days,date,date_to)
            VALUES (%s , %s , %s , %s ,%s , %s )
        ''' ,(book_title , student_name , student_class ,days,today_date,to_date))

        self.cur.execute('''
            UPDATE dayoperations_student,book SET book.book_issued="YES" WHERE dayoperations_student.book_name=book.book_name;
            ''' )
        self.db.commit()
        
        self.cur.execute('''
            SET @num := 0;

            UPDATE dayoperations_student SET id = @num := (@num+1);

            ALTER TABLE book AUTO_INCREMENT = 1;
            
            ''' )
        
        
        self.statusBar().showMessage('New Operation Added')

        self.show_book_combo()

        self.lineEdit_29.setText('')
        self.lineEdit_57.setText('')
        self.comboBox_2.setCurrentIndex(0)
        self.ShowAllBooks()
        self.Show_All_Operations_Student()
        

    def updateOperation_Student(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        index = self.tableWidget.selectionModel().currentIndex()
        row = index.row()
        row_ = row+1
        
        #########Taking values############ 
        value_title = index.sibling(index.row(),0).data()
        value_name = index.sibling(index.row(),1).data()
        value_class = index.sibling(index.row(),2).data()
        value_issued = index.sibling(index.row(),3).data()
        value_from = index.sibling(index.row(),4).data()
        value_to = index.sibling(index.row(),5).data()

        #########Setting the values########### 
        book_title = value_title
        book_issued = value_issued
        book_class = value_class
        book_name = value_name
        book_from = value_from
        book_to = value_to


        # print(value)
        self.cur.execute('''
            UPDATE dayoperations_student SET book_name=%s,student_name=%s,student_class=%s,book_issued=%s,date=%s,date_to=%s WHERE id = %s            
        ''', (book_title, book_name,book_class,book_issued,book_from,book_to,row_))
        self.cur.execute('''UPDATE book,dayoperations_student SET book.book_issued=dayoperations_student.book_issued WHERE dayoperations_student.book_name=book.book_name''')
        self.db.commit()
        self.show_book_combo()
        self.statusBar().showMessage('Book Updated')
        self.ShowAllBooks()

    def HandleOperationsTeacher(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        book_title = self.comboBox_4.currentText()
        teacher_name = self.lineEdit_56.text()
        teacher_subject = self.lineEdit_58.text()
        days = self.comboBox_8.currentIndex() + 1
        today_date = datetime.date.today()
        to_date = today_date + datetime.timedelta(days=days)

        self.cur.execute('''
            INSERT INTO dayoperations_teacher(book_name,teacher_name,teacher_subject,days,date,date_to)
            VALUES (%s , %s , %s , %s ,%s , %s )
        ''' ,(book_title , teacher_name , teacher_subject ,days,today_date,to_date))
        self.cur.execute('''
            UPDATE dayoperations_teacher,book SET book.book_issued="YES" WHERE dayoperations_teacher.book_name=book.book_name;
            ''' )
        self.db.commit()
        self.cur.execute('''
            SET @num := 0;

            UPDATE dayoperations_teacher SET id = @num := (@num+1);

            ALTER TABLE book AUTO_INCREMENT = 1;
            
            ''' )

        self.statusBar().showMessage('New Operation Added')

        self.lineEdit_56.setText('')
        self.lineEdit_58.setText('')
        self.comboBox_8.setCurrentIndex(0)
        self.show_book_combo()
        self.ShowAllBooks()
        self.Show_All_Operations_Teacher()

    def updateOperation_Teacher(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        index = self.tableWidget_3.selectionModel().currentIndex()
        row = index.row()
        row_ = row+1
        
        #########Taking values############ 
        value_title = index.sibling(index.row(),0).data()
        value_name = index.sibling(index.row(),1).data()
        value_subject = index.sibling(index.row(),2).data()
        value_issued = index.sibling(index.row(),3).data()
        value_from = index.sibling(index.row(),4).data()
        value_to = index.sibling(index.row(),5).data()

        #########Setting the values########### 
        book_title = value_title
        book_issued = value_issued
        book_subject = value_subject
        book_name = value_name
        book_from = value_from
        book_to = value_to

        # print(value)
        self.cur.execute('''
            UPDATE dayoperations_teacher SET book_name=%s,teacher_name=%s,teacher_subject=%s,book_issued=%s,date=%s,date_to=%s WHERE id = %s            
        ''', (book_title, book_name,book_subject,book_issued,book_from,book_to,row_))

        self.cur.execute('''UPDATE book,dayoperations_teacher SET book.book_issued=dayoperations_teacher.book_issued WHERE dayoperations_teacher.book_name=book.book_name''')
        self.db.commit()
        self.show_book_combo()
        self.statusBar().showMessage('Book Updated')
        self.ShowAllBooks()

    
    def Book_Not_Issued_Teacher(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT book_name , teacher_name , date , date_to FROM dayoperations_teacher WHERE book_returned="NO" && NOW()>date_to 
        ''')

        data = self.cur.fetchall()

        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)
        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget_4.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_position)
    
    def Book_Not_Issued_Student(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT book_name , student_name , date , date_to FROM dayoperations_student WHERE book_returned="NO" && NOW()>date_to 
        ''')

        data = self.cur.fetchall()

        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)
        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget_6.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)
        


    #################################
    #############Books###############

    def ShowAllBooks(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()
        
        self.cur.execute('''SELECT book_name,book_description,book_code,book_issued,book_category,book_author,book_publisher,book_price FROM book ''' )
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
            self.cur.execute('''
            SET @num := 0;

            UPDATE book SET id = @num := (@num+1);

            ALTER TABLE book AUTO_INCREMENT = 1;
            
            ''' )
        self.ShowAllBooks()

    def updateSelected(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        index = self.tableWidget_5.selectionModel().currentIndex()
        row = index.row()
        row_ = row+1
        
        #########Taking values############ 
        value_title = index.sibling(index.row(),0).data()
        value_description = index.sibling(index.row(),1).data()
        value_code = index.sibling(index.row(),2).data()
        value_issued = index.sibling(index.row(),3).data()
        value_category = index.sibling(index.row(),4).data()
        value_author = index.sibling(index.row(),5).data()
        value_publisher = index.sibling(index.row(),6).data()
        value_price = index.sibling(index.row(),7).data()
        
        #########Setting the values########### 
        book_title = value_title
        book_code = value_code
        book_issued = value_issued
        book_description = value_description
        book_category = value_category
        book_author = value_author
        book_publisher = value_publisher
        book_price = value_price


        # print(value)
        self.cur.execute('''
            UPDATE book SET book_name=%s,book_description=%s,book_code=%s,book_issued=%s,book_category=%s,book_author=%s,book_publisher=%s,book_price=%s WHERE id = %s            
        ''', (book_title, book_description,book_code,book_issued,book_category,book_author,book_publisher,book_price,row_))
        self.db.commit()
        self.show_book_combo()
        self.statusBar().showMessage('Book Updated')

    def Addnewbook(self):
        
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        id = self.lineEdit_30.text()
        book_title = self.lineEdit_2.text()
        book_code = self.lineEdit_3.text()
        book_description = self.textEdit.toPlainText()
        book_issued = self.comboBox_7.currentText()
        book_category = self.comboBox_3.currentText()
        book_author = self.lineEdit_41.text()
        book_publisher = self.lineEdit_42.text()
        book_price = self.lineEdit_4.text()

        self.cur.execute('''
            INSERT INTO book(id,book_name,book_description,book_code,book_issued,book_category,book_price,book_author,book_publisher)
            VALUES (%s ,%s , %s , %s , %s ,%s , %s , %s , %s)
        ''' ,(id,book_title , book_description , book_code , book_issued ,book_category , book_price , book_author , book_publisher,))

        self.db.commit()
        self.statusBar().showMessage('New Book Added')

        self.lineEdit_2.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_3.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.lineEdit_41.setText('')
        self.lineEdit_42.setText('')
        self.lineEdit_4.setText('')
        self.show_book_combo()
        
        self.ShowAllBooks()


    def searchbooks(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()
        
        book_title = self.lineEdit_5.text()

        sql = '''SELECT book_name,book_description,book_code,book_issued,book_category,book_author,book_publisher,book_price FROM book WHERE book_name=%s'''
        if self.cur.execute(sql , [(book_title)],):
            data = self.cur.fetchall()
            self.tableWidget_8.setRowCount(0)
            self.tableWidget_8.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_8.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_8.rowCount()
                self.tableWidget_5.insertRow(row_position)


            self.db.close()


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

    def show_category_combo(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()
        
        self.cur.execute(''' SELECT category FROM category ''')
        data = self.cur.fetchall()  

        self.comboBox_3.clear()
        for category in data :
            self.comboBox_3.addItem(category[0])
            # self.comboBox_5.addItem(category[0])

    def show_book_combo(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()
        
        self.cur.execute('''SELECT book_name FROM book WHERE book_issued="NO" ''')
        data = self.cur.fetchall()  

        self.comboBox.clear()
        self.comboBox_4.clear()
        for category in data :
            self.comboBox.addItem(category[0])
            self.comboBox_4.addItem(category[0])


    def show_issued_combo(self):
        self.comboBox_7.addItem("NO")
        self.comboBox_7.addItem("YES")

    #################################
    #############Users###############

    def Add_New_User(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        username = self.lineEdit_9.text()
        email = self.lineEdit_10.text()
        password = self.lineEdit_11.text()
        password2 = self.lineEdit_12.text()

        if password == password2 :
            self.cur.execute(''' 
                INSERT INTO users(user_name , user_email , user_pass)
                VALUES (%s , %s , %s)
            ''' , (username , email , password))

            self.db.commit()
            self.statusBar().showMessage('New User Added')

        else:
            self.label_30.setText('please add a valid password twice')

    
    def login(self):    
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        username = self.lineEdit_14.text()
        password = self.lineEdit_13.text()

        sql = '''SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[1] and password == row[3]:
                # print('user match')
                self.statusBar().showMessage('Valid Username & Password')
                self.groupBox_4.setEnabled(True)

                self.lineEdit_17.setText(row[1])
                self.lineEdit_15.setText(row[2])
                self.lineEdit_16.setText(row[3])
    
    def Edituser(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()
        
        username = self.lineEdit_17.text()
        email = self.lineEdit_15.text()
        password = self.lineEdit_16.text()
        password2 = self.lineEdit_18.text()

        original_name = self.lineEdit_14.text()

        if password == password2 :
            self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
            self.cur = self.db.cursor()

            self.cur.execute('''
                UPDATE users SET user_name=%s , user_email=%s , user_pass=%s WHERE user_name=%s
            ''', (username , email , password , original_name))

            self.db.commit()
            self.statusBar().showMessage('User Data Updated Successfully')

        else:
            self.statusBar().showMessage('User Data NOT Updated ')
            # print('make sure you entered you password correctly')

    def Export_Books(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT book_code,book_name,book_description,book_category,book_author,book_publisher,book_price FROM book''')
        data = self.cur.fetchall()

        wb = Workbook('all_books.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0 , 'Book Code')
        sheet1.write(0,1 , 'Book Name')
        sheet1.write(0,2 , 'Book Description')
        sheet1.write(0,3 , 'Book Category')
        sheet1.write(0,4 , 'Book Author')
        sheet1.write(0,5 , 'Book publisher')
        sheet1.write(0,6 , 'Book Price')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Book Report Created Successfully')

    def Export_Day_Operation_Student(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT book_name , student_name , student_class , book_issued ,date , date_to FROM dayoperations_student
        ''')

        data = self.cur.fetchall()
        wb = Workbook('day_operations.xlsx')
        sheet1  = wb.add_worksheet()

        sheet1.write(0,0,'book title')
        sheet1.write(0,1,'student name')
        sheet1.write(0,2,'student class')
        sheet1.write(0,3,'book issued')
        sheet1.write(0,4,'from - date')
        sheet1.write(0,5,'to - date')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')

    def Export_Day_Operation_Teacher(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT book_name , teacher_name , teacher_subject , book_issued ,date , date_to FROM dayoperations_teacher
        ''')

        data = self.cur.fetchall()
        wb = Workbook('day_operations_teacher.xlsx')
        sheet1  = wb.add_worksheet()

        sheet1.write(0,0,'book title')
        sheet1.write(0,1,'teacher name')
        sheet1.write(0,2,'teacher subject')
        sheet1.write(0,3,'book issued')
        sheet1.write(0,4,'from - date')
        sheet1.write(0,5,'to - date')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')

    def Export_Day_Operation_Student_Returned(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT book_name , student_name , date , date_to FROM dayoperations_student WHERE book_returned="NO" && NOW()>date_to 
        ''')

        data = self.cur.fetchall()
        wb = Workbook('day_operations_std_not_returned.xlsx')
        sheet1  = wb.add_worksheet()

        sheet1.write(0,0,'book title')
        sheet1.write(0,1,'student name')
        sheet1.write(0,2,'from - date')
        sheet1.write(0,3,'to - date')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')

    def Export_Day_Operation_Teacher_Returned(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',password='',db='library',port=3306)
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT book_name , teacher_name , date , date_to FROM dayoperations_teacher WHERE book_returned="NO" && NOW()>date_to 
        ''')

        data = self.cur.fetchall()
        wb = Workbook('day_operations_teacher_not_returned.xlsx')
        sheet1  = wb.add_worksheet()

        sheet1.write(0,0,'book title')
        sheet1.write(0,1,'teacher name')
        sheet1.write(0,2,'from - date')
        sheet1.write(0,3,'to - date')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')



    def Dark_Blue_Theme(self):
        style = open('themes/darkblue.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        style = open('themes/darkgray.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def QDark_Theme(self):
        style = open('themes/qdark.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
        