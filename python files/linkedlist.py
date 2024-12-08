
# For creating a single linked list firt we have to create a node 
class Node:
    def __init__(self,data) -> None:
        self.data= data
        self.next= None
# after cfreating anode we have to assign the head value and for the first time that will be none type
class SingleLinkedlist:
    def __init__(self) -> None:
        self.head=None
#  here we r displaying the linked list usng the had and assigning the head to temp and through this we are iterating the temp upto last node
    def display(self):
        temp=self.head
        if self.head is None:
            print("List is empty")
        else:
            while temp:
                print(temp.data,"-->", end=" ")
                temp=temp.next
            # print(temp.next)

#  adding the new node at begining   
    def InsertAtBegining(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

#  adding the new node at end   

    def Insert_end(self,data):
        endnode=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=endnode

#  adding the new node at index position

    def Insert_position(self,index,data):
        nodepos=Node(data)
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        nodepos.next=temp.next
        temp.next=nodepos
    
    def get_length(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        return count
    
    # def insert_values(self,data_list):
    #     self.head=None
    #     for data in data_list:
    #         self.Insert_end(data)

    def remove_value(self,index):
        
        if index>0 and index>=self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.head=self.head.next
        temp=self.head
        count=0
        while temp:
            if count == index-1:
                temp.next =temp.next.next
                break    
            temp=temp.next
            count=count+1


       



            

L1=SingleLinkedlist()
N1=Node(10)

# first node value is always the head so assigning the node to head 
L1.head=N1
# print("head1", head)
#  for the first node we dont have the next (address) value 
# after creating the node 2 only we get the address oof that value 
# so we are assigning the node2 address to the next value in the node 1
N2=Node(78)
N1.next=N2

N3=Node(89)
N2.next=N3

N4=Node(90)
N3.next=N4

L1.InsertAtBegining(34)
L1.InsertAtBegining(4)
L1.Insert_end(78)
L1.Insert_position(4,"io")
L1.Insert_position(7,"uoi")
print("length",L1. get_length())
print("beforeremoval", L1.display())
# L1.insert_values(["sow","mya",90,87,213])

# print("N2=", N2)
# print("N1", N1)
# print("next=",N1.next)

# print("D1", N1.data)
L1.remove_value(5)
L1.display()
 