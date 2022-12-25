from Book import clrscreen
from MenuLib import MenuBook, MenuMember, MenuIssueReturn

import issue

while True:
    from Book import clrscreen

    clrscreen.clrscreen()
    print("\t\t\t Library Management \n")
    print("_____________________________")
    print("1. Book Management")
    print("2. Members Management")
    print("3. Issue / Return Book")
    print("4. Exit")
    print("_____________________________")
    choice = int(input("Enter Choice between 1 to 4 :"))
    if choice == 1:
        MenuBook.MenuBook()
    elif choice == 2:
        MenuMember.MenuMember()
    elif choice == 3:
        MenuIssueReturn.MenuIssueReturn()
    elif choice == 4:
        break
    else:
        print("Wrong Choice .....Enter Your Choice again")
        x = input("Enter any key to continue")

# MODULE: MENULIB
from Book import clrscreen, display, insertData, deleteBook, SearchBookRec, UpdateBook
import Member
import issue


def MenuBook():
    while True:
        clrscreen.clrscreen()
        print("\t\t\tBook Record Management\n")
        print("------------------------------")
        print("1. Add Book Record")
        print("2. Display Book Records")
        print("3. Search Book Record")
        print("4. Delete Book Record")
        print("5. Update Book Record")
        print("6. Return to Main Menu")
        print("----------------------")
        choice = int(input("Enter Choice between 1 to 5 :"))
        if choice == 1:
            insertData.insertData()
        elif choice == 2:
            display.display()
        elif choice == 3:
            SearchBookRec.SearchBookRec()
        elif choice == 4:
            deleteBook.deleteBook()
        elif choice == 5:
            UpdateBook.UpdateBook()
        elif choice == 6:
            return
        else:
            print("Wrong Choice. Enter Your Choice again")
            x = input("Enter any key to continue")


from Book import clrscreen
from Member import insertMember, display, searchMember, deleteMember, updateMember
import issue


def MenuMember():
    while True:
        clrscreen.clrscreen()
        print("\t\t\t Member Record Management\n")
        print("---------------------------------")
        print("1. Add Member Record")
        print("2. Display Member Records")
        print("3. Search Member Record")
        print("4. Delete Member Record")
        print("5. Update Member Record")
        print("6. Return to Main Menu")
        print("----------------------")
        choice = int(input("Enter choice between 1 to 5:"))
        if choice == 1:
            insertMember.insertMember()
        elif choice == 2:
            display.display()
        elif choice == 3:
            searchMember.searchMember()
        elif choice == 4:
            deleteMember.deleteMember()
        elif choice == 5:
            updateMember.updateMember()
        elif choice == 6:
            return
        else:
            print("Wrong Choice ..... Enter Your Choice again")
            x = input("Enter any key to continure")


from Book import clrscreen
import Member
from issue import issueBook, ShowIssueBooks, returnBook


def MenuIssueReturn():
    while True:
        clrscreen.clrscreen()
        print("\t\t\t Issue Record Management\n")
        print("---------------------------------")
        print("1. Issue Book")
        print("2. Display Issued Book Records")
        print("3. Return Issued Book")
        print("4. Return to Main Menu")
        print("----------------------")
        choice = int(input("Enter Choice between 1 to 4:"))
        if choice == 1:
            issueBook.issueBook()
        elif choice == 2:
            ShowIssueBooks.ShowIssueBooks()
        elif choice == 3:
            returnBook.returnBook()
        elif choice == 4:
            return
        else:
            print("Wrong Choice ..... Enter Your Choice again")
            x = input("Enter any key to continure")


# MODULE: BOOK

import os
import platform


def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))


import mysql.connector
from mysql.connector import errorcode
# from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os


# import platform

def display():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='Library')
        Cursor = cnx.cursor()
        query = ("SELECT * from bookRecord")
        Cursor.execute(query)

        for (Bno, Bname, Author, price, publ, qty, d_o_purchase) in Cursor:
            print("---------------------------------------------------------")
            print("Book Code:", Bno)
            print("Book Name:", Bname)
            print("Author of Book:", Author)
            print("Price of Book:", price)
            print("Publisher:", publ)
            print("Total Quantity in hand:", qty)
            print("Purchased on:", d_o_purchase)
            print("---------------------------------------------------------")
        Cursor.close()
        cnx.close()
        print("You have done it!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os
import platform


def insertData():
    try:
        cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code:")
        bname = input("Enter Book Name:")
        Auth = input("Enter Book Author's Name:")
        price = int(input("Enter Book Price:"))
        publ = input("Enter Publisher of Book:")
        qty = int(input("Enter Quantity purchased:"))
        print("Enter Date of Purchase (Date/Month and Year separately):")
        DD = int(input("Enter Date:"))
        MM = int(input("Enter Month:"))
        YY = int(input("Enter year:"))
        Qry = ("insert into bookRecord Values(%s,%s,%s,%s,%s,%s,%s)")
        data = (bno, bname, Auth, price, publ, qty, date(YY, MM, DD))
        Cursor.execute(Qry, data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


import mysql.connector
from mysql.connector import errorcode
# from datetime import date, datetime, timedelta
from mysql.connector import (connection)


# import os
# import platform

def deleteBook():
    try:
        cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code of Book to be deleted from the Library:")
        Qry = ("delete from BookRecord where bno = %s")
        del_rec = (bno,)
        Cursor.execute(Qry, del_rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record deleted successfully")
    except mysql.connector.Error as err:
        if err.errno == errocode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os
import platform


def SearchBookRec():
    try:
        cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book No to be Searched from the Library:")
        query = ("select * from BookRecord where bno = %s")
        rec_srch = (bno,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for (Bno, Bname, Author, price, publ, qty, d_o_purchase) in Cursor:
            Rec_count += 1
            print("---------------------------------------------------------")
            print("Book Code:", Bno)
            print("Book Name:", Bname)
            print("Author of Book:", Author)
            print("Price of Book:", price)
            print("Publisher:", publ)
            print("Total Quantity in hand:", qty)
            print("Purchased on:", d_o_purchase)
            print("---------------------------------------------------------")
            if Rec_count % 2 == 0:
                input("Press any key to continue")
                clrscreen()
                print(Rec_count, "Record found")
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errocode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os
import platform


def UpdateBook():
    try:
        cnx = connection.MySQLConnection(user='root', password='1234',
                                         host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book No to be Updated from the Library:")
        query = ("select * from BookRecord where bno = %s")
        rec_srch = (bno,)
        print("Enter new data")
        bname = input("Enter Book Name:")
        Auth = input("Enter Book Author's Name:")
        price = int(input("Enter Book Price:"))
        publ = input("Enter Publisher of Book:")
        qty = int(input("Enter Quantity purchased:"))
        print("Enter Date of Purchase (Date/Month and Year separately):")
        DD = int(input("Enter Date:"))
        MM = int(input("Enter Month:"))
        YY = int(input("Enter Year:"))
        Qry = ("update BookRecord set bname = %s, Auth = %s, price = %s, publ = %s, qty = %s, date = %s where bno = %s")
        data = (bname, Auth, price, publ, qty, date(YY, MM, DD), bno)
        Cursor.execute(Qry, data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record updated successfully")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()
        UpdateBook()


# MODULE: ISSUE

import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os


def clrscreen():
    print('\n' * 5)


import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os


def ShowIssueBooks():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='Library')
        Cursor = cnx.cursor()
        query = (
            "select b.bno,bname,m.mno,m.mname,i.doi,i.dor from bookRecord b, issue i, member m where b.bno=i.bno and i.mno = m.mno")
        Cursor.execute(query)

        for (Bno, Bname, Mno, Mname, doi, dor) in Cursor:
            print("---------------------------------------------------------")
            print("Book Code:", Bno)
            print("Book Name:", Bname)
            print("Member Code:", Mno)
            print("Member name:", Mname)
            print("Date of issue:", doi)
            print("Date of return:", dor)
            print("---------------------------------------------------------")

        Cursor.close()
        cnx.close()
        print("you have done it.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os


def issueBook():
    try:
        cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code to issue:")
        mno = input("Enter Member Code:")
        print("Enter Date of Issue (Date/Month and Year separately):")
        DD1 = int(input("Enter Date:"))
        MM1 = int(input("Enter Month:"))
        YY1 = int(input("Enter Year:"))
        print("Enter Date of Return (Date/Month and Year separately):")
        DD2 = int(input("Enter Date:"))
        MM2 = int(input("Enter Month:"))
        YY2 = int(input("Enter Year:"))
        Qry = ("insert into issue (bno, mno,doi,dor) values (%s, %s, %s, %s)")
        data = (bno, mno, date(YY1, MM1, DD1), date(YY2, MM2, DD2))

        Cursor.execute(Qry, data)
        cnx.commit()
        cnx.close()
        print("Record inserted")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os


def returnBook():
    try:
        cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code to be returned to the library:")
        mno = input("Enter Member Code of member who is returning book:")
        dor = input("Enter date of return:")
        Qry = ("delete from issue where bno = %s and mno = %s")
        rec = (bno, mno)
        Cursor.execute(Qry, rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record deleted successfully")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


# MODULE: MEMBER

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os


def clrscreen():
    print('\n' * 5)


import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os


def display():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='Library')
        Cursor = cnx.cursor()
        query = ("select * from member")
        Cursor.execute(query)

        for (Mno, Mname, Mob, DOM, ADR) in Cursor:
            print("---------------------------------------------------------")
            print("Member Code:", Mno)
            print("Member Name:", Mname)
            print("Mobile no. of member:", Mob)
            print("Date of membership:", DOM)
            print("Address:", ADR)
            print("---------------------------------------------------------")
        Cursor.close()
        cnx.close()
        print("you have done it.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os


def insertMember():
    try:
        cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='Library')
        Cursor = cnx.cursor()
        mno = input("Enter Member Code:")
        mname = input("Enter member name:")
        mob = input("Enter member mobile no:")
        print("Enter Date of Membership (Date/Month and Year separately):")
        DD = int(input("Enter Date:"))
        MM = int(input("Enter Month:"))
        YY = int(input("Enter Year:"))
        addr = input("Enter member address:")
        Qry = ("insert into member values(%s, %s, %s, %s, %s)")
        data = (mno, mname, mob, date(YY, MM, DD), addr)
        Cursor.execute(Qry, data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record inserted")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os


def deleteMember():
    try:
        cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='Library')
        Cursor = cnx.cursor()
        mno = input("Enter Member Code to be deleted from the library:")
        Qry = ("delete from member where mno = %s")
        del_rec = (mno,)
        Cursor.execute(Qry, del_rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record deleted successfully")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os


def searchMember():
    try:
        cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='Library')
        Cursor = cnx.cursor()
        mnm = input("Enter member name to be searched:")
        query = ("select * from Member where mname = %s")
        rec_srch = (mnm,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for (Mno, Mname, Mob, DOP, ADR) in Cursor:

            print("---------------------------------------------------------")
            print("Member Code:", Mno)
            print("Member Name:", Mname)
            print("Mobile no. of member:", Mob)
            print("Date of membership:", DOP)
            print("Address:", ADR)
            print("---------------------------------------------------------")
            if Rec_count % 2 == 0:
                input("Press any key to continue")
            Rec_count += 1

        print(Rec_count, "Record found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()
