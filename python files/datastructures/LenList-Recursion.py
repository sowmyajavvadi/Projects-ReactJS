def length(l):
    if l==[]:
        return 0
    else:
        return (1+len(l[1:]))
l=[2,3,4,5]
print(l[2:])
print(length(l))