import sys
from array import *
queue=array('i',[])
def enqueue():
    element=int(input("enter element:"))
    queue.append(element)
    print(element,"is added to queue")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop()
        print("removed element is",e)
def display():
    print("the elements in queue is:")
    for i in queue:
        print(i)
while True:
    print("select the operation 1.add 2.remove 3.show 4.quit")
    choice =int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        dequeue()
    elif choice==4:
        break
    else:
        print("enter correct operation")