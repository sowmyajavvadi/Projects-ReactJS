n=int(input("ener value=="))

def Prime(a):
    count=0
    for i in range(1,a):
        if a%i==0:
            count=count+1
        continue
    if count>2:
        print("prime")
    else:
        print("not a prime")
print(Prime(n))
