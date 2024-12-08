a=[100,20,50,10,9,82,69,1]
for i in range(len(a)):
    min_index=i
    # print(min_index,"Min Index")
    for j in range(i+1,len(a)):
        if a[min_index]>a[j]:
            min_index=j
    a[i],a[min_index]=a[min_index],a[i]
for i in range(len(a)):
 print(a[i])