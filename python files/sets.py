# sai=set()
# print(type(sai))

# sowmya={0,2,3,54,56,7,8,9,"python",False}
# print(sowmya)

# set methods
'''
sow={21,45,"no",876,9,87,4,1,3,6,9,9,5,6}
sow.add(5463656)
sow.update({12,"python"})
sow.remove("no")
print("pop",sow.pop())
bow=sow.copy()
print("copy",bow)
print(sow)


#set Operators

set1={1,2,3,45,6,5,10,60,77}
set2={10,5,60,77}
print("union",set1.union(set2))
print("Intersection",set1.intersection(set2))
print("difference",set1.difference(set2))
print("Symmetric-difference",set1.symmetric_difference(set2))
print("isdisjoint",set1.isdisjoint(set2))
print("issuperset", set1.issuperset(set2))
print("issubset",set2.issubset(set1))


'''


f={1,3,1,32,31,412,4,31}
for i in f:
    print(i**2)

print([i**2 for i in {1,3,1,32,31,412,4,31}])


g=[13,12,4,15,245,12,11,1,1,11,4,2,2,3,3,4]
f=[]
for i in g:
    if i not in f:
        f.append(i)
print(f)


#froozen set--freeze

l=[1,2,3,4,5,6,7,9]
l.append(2345)
print("l",l)
d=frozenset(l)
# d.append(43534)
print("d",type(d))