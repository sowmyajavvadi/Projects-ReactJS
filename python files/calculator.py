a=int(input("enter the value="))
b=int(input("enter the value="))
result=0
userinput=int(input("select any operation \n 1.addition \n 2.Substraction \n 3.Multiplication \n 4.division \n"))
if userinput==1:
    result=a+b
    print(result)
elif userinput==2:
    result=a-b
    print(result)
elif userinput==3:
    result=a*b
    print(result)
else:
    result=a/b
    print(result)