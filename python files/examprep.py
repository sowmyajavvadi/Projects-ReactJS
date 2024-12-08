def f(n):
    s = 0
    for i in range(2,n):
        if n%i == 0 and i%2 == 1:
            s = s+1
    return(s)
# print(f(90))
# print(f(89))

x = ["slithy",[7,10,12],2,"tove",1] 
x[0] = x[0][:5] + 'ery'
x[1][0] = 5555                     # Statement 9

# print(x)

# def mystery(l):
#   l = l[1:]
#   return()

# mylist = [7,11,13]
# print(mystery(mylist))

# def mystery(l):
#     if l == []:
#         return(l)
#     else:
#         return(l[-1:]+mystery(l[:-1]))
# print(mystery([23,35,19,58,93,46]))

l=[23,35,19,58,93,46]
print(l[0:5:3])
mystring="sowmyajavvadi"
print(mystring[1:5])