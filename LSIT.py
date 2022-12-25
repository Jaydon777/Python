'''def Convert(string):
    l = list(string.split(" "))
    return l
   
str1 = input("Enter a string:")
print(Convert(str1))'''

'''a = 'TajMahal'
count = 0
for letter in a:
    if letter == 'a':
        count+=1
print(count)'''

import re
text = "Hello world"
a = re.findall("^Hello",text)
if (a):
    print("Yes")
else:
    print("No")

