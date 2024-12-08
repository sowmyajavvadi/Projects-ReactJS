from datetime import date

# name=str(input("Enter the customer name: "))
listofitems='''
 Rice    RS 20/kg
 sugar   RS 40/kg
 milk    RS 15/pkg
 boost   RS 20/kg
 colgate RS 40/pkg
 salt    RS 30/kg
 tomato  RS 50/kg
 pepper  RS 10/pkg
 onions  RS 60/kg
 ginger  RS 20/kg
'''
# declarations
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=0
qlist=[]
plist=[]


items={
    'rice':20,
    'sugar':40,
    'milk':15,
    'boost':20,
    'colgate':40,
    'salt':30,
    'tomato':50,
    'pepper':10,
    'onions':60,
    'ginger':20

}

option=int(input("for list of items press 1:"))
if option==1:
    print(listofitems)
for i in range(len(listofitems)):
    inpt1=int(input("if you want to buy the items press 1 oor 2 for exit"))
    if inpt1==2:
        break
    if inpt1==1:
        item=


    