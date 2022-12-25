def dictionary(d,n):
 for i in range(0,n+1):
     d[i]=i**3
     print(d)
    
 
d=dict()
n = int(input("Number of elements in the dictionary:"))
dictionary(d,n)
print(d.keys())
print(d.values())
