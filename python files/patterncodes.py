'''

for i in range(1,8):
    for j in range(i):
        print(i,end=" ")
    print()

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 6 6 
# 7 7 7 7 7 7 7 

for i in range(1,8):
    for j in range(i):
        print(j,end=" ")
    print()
# 0 
# 0 1 
# 0 1 2 
# 0 1 2 3 
# 0 1 2 3 4 
# 0 1 2 3 4 5 
# 0 1 2 3 4 5 6 

for i in range(1,8):
    for j in range(i+1):
        print(i,end=" ")
    print()

# 1 1 
# 2 2 2 
# 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 5 
# 6 6 6 6 6 6 6 
# 7 7 7 7 7 7 7 7 

for i in range(1,8):
    for j in range(i+1):
        print(j,end=" ")
    print()

# 0 1 
# 0 1 2 
# 0 1 2 3 
# 0 1 2 3 4 
# 0 1 2 3 4 5 
# 0 1 2 3 4 5 6 
# 0 1 2 3 4 5 6 7 


for i in range(5):
    for j in range(i):
        print(j,end=" ")
    print()

# 0 
# 0 1 
# 0 1 2 
# 0 1 2 3 

for i in range(5):
    for j in range(i):
        print('*',end=" ")
    print()

# * 
# * * 
# * * * 
# * * * * 


for i in range(6,0,-1):
    for j in range(0,i):
        print(j,end=" ")
    print()

# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1 
# 0 

for i in range(6,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print()

# 6 6 6 6 6 6 
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 
'''
m=0
for i in range(6,0,-1):
    m=m+1
    for j in range(i):
        print(m,end=" ")
    print()

# 1 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 
# 4 4 4 
# 5 5 
# 6 

m=7
for i in range(6,0,-1):
    for j in range(i):
        print(m,end=" ")
    print()
    
# 7 7 7 7 7 7 
# 7 7 7 7 7 
# 7 7 7 7 
# 7 7 7 
# 7 7 
# 7 
