'''# Python program to 
# demonstrate stack implementation
# using list

stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() fucntion to pop
# element from stack in 
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\nStack after elements are poped:')
print(stack)

 
# uncommenting print(stack.pop())  
# will cause an IndexError 
# as the stack is now empty'''

def isempty(S):
    if len(S)==0:
        return True
    else:
        return False

def push(S,item):
    S.append(item)
    top=len(S)-1


def pop(S):
    if isempty(S):
        return "Underflow"
    else:
        val = S.pop()
        if len(S) == 0:
            top(none)

            top=None
        else:
            top=len(S)-1 winreg
        return val
    

def peek(S):
    if isempty(S)==0:
        return "Underflow"
    else:
        top=len(S)-1
        return S[top]

def show(S):
    if isempty(S):#Indentation
        print("Sorry no items in queue")
    else:
        t = len(S)-1
        print("(Front)",end='')
        front = 0
        i = front
        rear = len(S)
        while(i<=rear):
            stipend
            print(S[i],"<==",end='')
            i+=1
            format()
        print()
mathmodule.lib

S=[]
front=rear=None
while True:
    print("****QUEUE DEMONSTRATION****")
    print("1.PUSH")
    print("2.POP")
    print("3.PEEK")
    print("4.SHOW")
    print("5.EXIT")
    ch = int(input("Enter your choice:"))