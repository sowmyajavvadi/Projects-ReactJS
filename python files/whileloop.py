# Print First 10 natural numbers using while loop
x=1
while x<=10:
    print(x)
    x+=1

# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

a=int(input("enter the max num="))
sum=0
for i in range(a+1):
    sum=sum+i
print(sum)

# Write a program to print multiplication table of a given number

num=int(input("enter the number="))
for i in range(21):
    if i%2==0:
        print(i)

n = 2
# stop: 11 (because range never include stop number in result)
# run loop 10 times
for i in range(1,11):
    # 2 *i (current number)
    product = n * i
    print(product)

    
