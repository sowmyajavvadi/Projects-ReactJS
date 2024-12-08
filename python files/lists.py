'''
x=[]
print(type(x))

surya=[1,2.2,'abc',True,7,8]
print(surya[3],surya[-3])
print(len(surya)  )
# sclicing[start:stop:skip]
print(surya[0:4])
print(surya[0:5:3])    #starts at 1 and stops at 4 skips 2 values
print(surya[5:0:-2])   #backward directionand backward skip
print(surya[-1:-4:-2])


sekar=[22,42,42,5,356,3,64,74,6]
print(sekar[:5])
print(sekar[5:])
print(sekar[::])
print(sekar[::-1])
print(sekar[:-2])

#list methods- append extend
venu=[14,1,42]
venu.append('boy') #append method--single element
venu.extend('boy')# extend --bulk elements
venu.extend([7,8,9])
print(venu)

# copy method
venu=[14,1,42,4,2,4,2]
v=venu.copy()# copy the values to variable but if there are any chnges in the new var will not refect in old var 
v.append(13234)
print(venu)

# clear method
venu=[14,1,42,4,2,4,2]
venu.clear()
print(venu)


# count method--takes atleast one arg
venu=[14,1,42,4,2,4,2]
print("4's=",venu.count(4)) # counts the no.of tyme the value in list is presnt
print("42's=",venu.count(42))
print("2's=",venu.count(2))


#insert method--take two args(index,value)
venu=[14,1,42,4,2,4,2]
venu.insert(0,3) #inserts the value at 0 index position
venu.insert(4,'sowmya')
print(venu)


#pop , remove
venu=[14,1,42,4,2,4,2]
venu.pop(2) #it takes the index values to remove thr elemrnts---removes the element at 2 index position
venu.remove(4) # it removes the elements based on the given value
print(venu)


# reverse method
venu=[14,1,42,4,2,4,2]
venu.reverse()
print(venu)



#sort method
venu=[14,1,42,4,2,4,2]
venu.sort()
print("ascending order",venu)
venu.sort(reverse=True)
print("descending order",venu)


#index
venu=[14,1,42,4,2,4,2]
print(venu.index(4))
print(venu.index(14))


#identify the index of duplicate elements
l=[1,2,3,343,56,56,343,99,87,88,99]
for i in range (len(l)):
    if l[i]==343:
        print(i)


#identify the index of duplicate elements and replace that element with another number
l=[1,2,3,343,56,56,343,99,87,88,99]
for i in range (len(l)):
    if l[i]==343:
        l[i]='sowmi'
        print(i)
print(l)

'''


#list comprehension
# print([("EVEN",i) if i%2==0 else "ODD" for i in range(0,10)])

# print([num+2 for num in [1,2,3,4,5,6,7,8]])

print ([num  for num in [-2,-1,0,1,2,3,4,5] if num >0])
