numbers=[1,2,3,4,5,1,2,3,4,5,6,7,8,9]
for i in range(len(numbers)):
    # print(len(numbers))
    for j in range(i+1,len(numbers)):
        # print(j)
        if numbers[i] == numbers[j]:
            # duplicate=numbers[i]
            print(numbers[i])
            
        
# for i in range(len(numbers)):
#     if numbers[i] == duplicate:
#         print(i)
 