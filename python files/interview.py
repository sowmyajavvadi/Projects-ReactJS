
# def pal(str):
#     if(str[::]==str[-1::]):
#         return 'palindrome'
#     else:
#         return 'non pal'
# result=pal('racecar')
# print(result)

arr=[1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
result=[]
def removedup(arr):
    for item in arr:
        if(arr[item]!=arr[item+1]):
            print(item)
            new_arr= result.append(item)
    print(new_arr) 
result=removedup(arr)
print("result",result)	