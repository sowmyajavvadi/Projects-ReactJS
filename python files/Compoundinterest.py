#compound interest formula=p(1+r/n)^nt

p=int(input("enter P value="))
n=int(input("enter n value="))
r=int(input("enter r value="))
t=int(input("enter t value="))

print("coumpound interest=",p*(1+(r/n))**(n*t))