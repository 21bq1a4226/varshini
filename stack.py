import sys
from array import *
a=array('i',[])
while True:
    print("1.push 2.pop 3.display 4.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        ele=int(input("enter element:"))
        a.append(ele)
        print("inserted")
    elif ch==2:
        if len(a)==0:
            print("stack is empty")
        else:
            print("deleted element is",a.pop())
    elif ch==3:
        if len(a)==0:
            print("stack is empty")
        else:
            print("the element in stack is:")
            for i in a:
                print (i)
    elif ch==4:
        sys.exit()
    else:
        print("invalid choice")