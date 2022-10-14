class node:
    def __init__(self,data):
        self.data=data
        self.ref=name
class linkedlist:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                h=n.ref
ll1=linkedlist()
ll1.print_ll()
