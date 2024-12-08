max=int(input("entermax num:"))

odd_numbers=[]

for i in range(1,max):
    if i%3==0:
        odd_numbers.append(i)

print("odd numbers=",odd_numbers)
