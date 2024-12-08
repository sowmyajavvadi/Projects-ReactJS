class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class Linkedlist:
    def __init__(self):
        self.head=None

    def Insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb


    

    def Insert_ending(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne


        



    def display(self):
        temp=self.head
        if self.head==None:
            print("list is empty")
        while temp:
            print(temp.data ,"-->",end=" " )
            temp=temp.next
L=Linkedlist()
N=Node(34)
L.head=N
L.Insert_beginning(8)
L.Insert_ending(89)
L.display()
