import csv

def readcsv():
    f = open(r'C:\Users\Admin\AppData\Local\Programs\Python\Python38\PROGS\data.csv','r')
    data = csv.reader(f)
    for row in data:
        print(row)

def writecsv():
    file = open(r'C:\Users\Admin\AppData\Local\Programs\Python\Python38\PROGS\data.csv',mode='w',newline='')
    writer = csv.writer(file,delimiter = ',')
    writer.writerow(['Rollno','Name','Marks'])
    ans = 'y'
    print("Enter student information")
    while ans == 'y':
        Rollno = int(input("Enter rollno:"))
        Name = input("Enter name:")
        Marks = float(input("Enter marks:"))
        rec = [Rollno,Name,Marks]
        writer.writerow(rec)
        ans = input("Do you want to continue-'y/n'?")

writecsv()
readcsv()

