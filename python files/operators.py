'''
# membership operators--in, not in
a=[1,2,3,4,5,6]
print(-2 in a)
print(2 in a)
print(45 not in a)


# identity operator ---is,  is not--checks the vars have same memory or data


a=[1,2,3,4,5,6]
a1=[1,2,3,4,5,6]
print(id(a)==id(a1))
print(a is  a1)
print(a is not a1)
b=1
c=1
print(b is c)


#example
num=[1,2,3,4,5,6,7,8,9,9,9,9,10]
num_to_remove=[1,9]
print([i for i in num if i not in num_to_remove])


#example2

lst=[]
n=int(input("enter no of elements"))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(lst)

'''
l=[1,2,3,4,5,18,19,2,0,20]
print(["valid to vote" if i==18 else "not eligible" for i in l])   #here in this logic it is checking every element and printing the result gor every elemrnt as i have given else also
print(["adult" for i in l if i==18]) # here it is checking all the lements and printg only if condition satistys