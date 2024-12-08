a=[12,56,67,34,65,2,14,9]
sortedlist=a.sort()
print(a)
high=len(a)-1
low=0
mid=0
target=int(input("enter the target"))
while low<=high:
    mid=(high+low)//2
    if a[mid]==target: 
        print(target,"position found",mid+1)
        break
    elif a[mid]>target:
        high=mid-1
    else:
        low=mid+1
else:
    print("not found")