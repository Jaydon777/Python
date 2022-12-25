import pickle
stu = { }
f = open(r"C:\Users\Admin\AppData\Local\Programs\Python\Python39\PROGS\new.dat","wb")
ans = 'y'
while ans == 'y':
     rno = int(input("Enter roll number:"))
     name = input("Enter name:")
     stu['Rollno'] = rno
     stu['Name'] = name
     pickle.dump(stu,f)

     ans = input("Want to enter more records? (y/n)...")
f.close()

f1 = open(r"C:\Users\Admin\AppData\Local\Programs\Python\*/Python39\PROGS\new.dat","rb")
found = False
srno = int(input("Enter the roll number to be searched:"))
try:
     print("Searching the roll number in Student file...")
     while True:
         
         stu = pickle.load(f1)
         if stu['Rollno'] == srno:
             print(stu['Name'])
             found = True
except EOFError:
     if found == False:
         print("No such roll number found in the file.")
     else:
         print("Roll number was found.")
f1.close()
print(eval)
