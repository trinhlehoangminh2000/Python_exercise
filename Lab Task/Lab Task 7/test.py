a = [4,5,4,5,1,2,3]
def selectionSort(a):
    #Iterate through array
    for i in range(len(a)):
        #Find the smallest element
        min = i
        for j in range(i+1 , len(a)):
            if a[j] < a[min]:
                min = j
        #Swap the smallest element with the first element 
        key = a[i]
        a[i] = a[min]
        a[min] = key 
    return a

    
print(selectionSort(a))