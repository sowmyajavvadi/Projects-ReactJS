def insertionSort(arr):
    for i in range(1,len(arr)):
        k=arr[i]
        j=i-1
        while j>=0 and k<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=k
            
	
arr = [12,87,67, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
