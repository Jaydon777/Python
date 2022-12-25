'''import mysql.connector as ms
con = ms.connect(host = "localhost", user = "root", passwd = "1234", database = "student")
cur = con.cursor()
cur.execute("Select * from exam")
#cur.execute("Insert into exam values(104,'Haniel','A','Art')")
#con.commit()
for i in cur:
    print(i)'''

a = 10
def call():
    global a
    a=15
    b=20
    print(a)
call()
