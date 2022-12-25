x,p1,p2,c= int(input()),int(input()),int(input()),int(input())
a = int((p1/100)*x)
raw1 = x-a
raw2 = int((raw1*100)/(100-p2))
print(raw2*c)