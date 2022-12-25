import mysql.connector as ms
con = mysql.connecter(host="localhost", user="root", passwd="1234",database="Tution")

cur = con.cursor()
cur.execute("Insert into Exam values(6,'Arun',850,'English')")
com.commit()
for i in cur:
    print(i)''

import mysql.connector as ms
con = ms.connect(host = 'localhost',user = 'root',passwd = '1234',database = 'transport')
cur = con.cursor()
cur.execute("Select * from trans")
for i in cur:
    print(i)

