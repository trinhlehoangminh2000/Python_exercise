import sys, time
from datetime import datetime

#NB the implementation of merge sort comes with comments; you can comment your own code, but this is optional
#NB2 the other sorts take less code! ;-)

#Swap function
def swap(a, b, c):
    key = a[b]
    a[b] = a[c]
    a[c]= key

#Insertion sort
def insertionSort(a):
    for i in range(len(a)):
        key = a[i]
        j = i
        while j>0 and a[j-1]>key:                               #Iterate backward 
            a[j] = a[j-1]                                       #if key is smaller than the previous: swap
            j -=1
        a[j] = key
    return a

#Buble sort
def bubbleSort(a):
    flag = True                                                 
    while flag is True: 
        flag = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                flag = True                                     #Flag only be set to True if there is abnomality
                swap(a, i, i+1)
    return a

#Merge sort
def mergeSort(alist):
    if len(alist)<=1:                                           #stopping condition             
        return alist                                            
    mid = len(alist)//2                                         #split list into 2
    lefthalf = alist[:mid]                                      #left half
    righthalf = alist[mid:]                                     #right half
    lefthalf = mergeSort(lefthalf)                              #recurse on left half, get sorted left half
    righthalf = mergeSort(righthalf)                            #recurse on right half, get sorted right half
    return merge(lefthalf, righthalf)                           #merge sorted left and right halves
def merge(lefthalf,righthalf):
    merged_list = [0] * (len(lefthalf) + len(righthalf))        
    i=0                                                         #three counters
    j=0
    k=0                                                 
    while i < len(lefthalf) and j < len(righthalf):     
        if lefthalf[i] <= righthalf[j]:                         #if element in left is less than or equal to element in right                                                    
            merged_list[k]=lefthalf[i]                          #add it to the merged list
            i=i+1                                               #move to the next item in the left list
        else:                                                                         
            merged_list[k]=righthalf[j]                         #otherwise move the element in the right list
            j=j+1                                               #to the merged list and move to the next item in the right list
        k=k+1                                                   #move to the next item in the merged list

    while i < len(lefthalf):                                    #if items are left over in the left half,                           
        merged_list[k]=lefthalf[i]                              #add to the merged list
        i=i+1
        k=k+1

    while j < len(righthalf):                                   #if items are left over in the right half,                         
        merged_list[k]=righthalf[j]                             #add to the merged list
        j=j+1
        k=k+1

    return merged_list

#Quick sort
def quickSort( mylist ):
    if mylist == []:                                            #stopping condition
        return []                                               #no elements in list; return empty list
    pivot = mylist[0]                                           #take first element of list as pivot
    ltp = quickSort([x for x in mylist[1:] if x < pivot])       #recurse on list of elements less than pivot (‘ltp’)
    etogtp = quickSort([x for x in mylist[1:] if x >= pivot])   #recurse on list of elements equal to or greater than pivot (‘etogtp’)
    return ltp + [pivot] + etogtp                               #return list concatenating ltp, pivot and etogtp

#Selection sort
def selectionSort(a):
    for i in range(len(a)):                                     #Iterate through array
        min = i                                                 #Find the smallest element
        for j in range(i+1 , len(a)):
            if a[j] < a[min]:
                min = j                                         #Swap the smallest element with the first element 
        swap(a, i, min) 
    return a

def main():
    #Calculating the time taken for insertion sort
    start = datetime.now()
    for i in range(10):  
        Hundred_list = [8, 32, 18, 53, 21, 23, 3, 81, 38, 14, 61, 7, 56, 31, 50, 44, 16, 17, 42, 57, 95, 55, 100, 78, 9, 68, 24, 75, 69, 96, 28, 84, 82, 2, 36, 94, 80, 15, 39, 99, 43, 25, 10, 87, 63, 41, 72, 65, 35, 12, 60, 33, 79, 90, 5, 51, 54, 74, 37, 40, 11, 93, 59, 98, 27, 49, 89, 83, 77, 86, 91, 97, 46, 1, 6, 76, 45, 73, 52, 88, 70, 13, 47, 85, 4, 34, 22, 20, 92, 62, 19, 64, 71, 66, 30, 26, 29, 58, 48, 67]
        res = insertionSort(Hundred_list)                                                                                 
    delta = (datetime.now() - start)/10
    print("Insertion sort took:     %s" %delta.total_seconds())
    print("Big O notation: Polynomial O(n^k)\n")
    
    #Calculating the time taken for bubble sort
    start = datetime.now()
    for i in range(10):  
        Hundred_list = [8, 32, 18, 53, 21, 23, 3, 81, 38, 14, 61, 7, 56, 31, 50, 44, 16, 17, 42, 57, 95, 55, 100, 78, 9, 68, 24, 75, 69, 96, 28, 84, 82, 2, 36, 94, 80, 15, 39, 99, 43, 25, 10, 87, 63, 41, 72, 65, 35, 12, 60, 33, 79, 90, 5, 51, 54, 74, 37, 40, 11, 93, 59, 98, 27, 49, 89, 83, 77, 86, 91, 97, 46, 1, 6, 76, 45, 73, 52, 88, 70, 13, 47, 85, 4, 34, 22, 20, 92, 62, 19, 64, 71, 66, 30, 26, 29, 58, 48, 67]
        res = bubbleSort(Hundred_list)                                                                                 
    delta = (datetime.now() - start)/10
    print("Bubble sort took:        %s" %delta.total_seconds())
    print("Big O notation: Polynomial O(n^k)\n")
    
    #Calculating the time taken for merge sort
    start = datetime.now()
    for i in range(10):
        Hundred_list = [8, 32, 18, 53, 21, 23, 3, 81, 38, 14, 61, 7, 56, 31, 50, 44, 16, 17, 42, 57, 95, 55, 100, 78, 9, 68, 24, 75, 69, 96, 28, 84, 82, 2, 36, 94, 80, 15, 39, 99, 43, 25, 10, 87, 63, 41, 72, 65, 35, 12, 60, 33, 79, 90, 5, 51, 54, 74, 37, 40, 11, 93, 59, 98, 27, 49, 89, 83, 77, 86, 91, 97, 46, 1, 6, 76, 45, 73, 52, 88, 70, 13, 47, 85, 4, 34, 22, 20, 92, 62, 19, 64, 71, 66, 30, 26, 29, 58, 48, 67]
        res = mergeSort(Hundred_list)                                                                                    
    delta = (datetime.now() - start)/10
    print("Merge sort took:         %s" %delta.total_seconds())
    print("Big O notation: Log linear O(n log n)\n")    

    #Calculating the time taken for quick sort
    start = datetime.now()
    for i in range(10):
        Hundred_list = [8, 32, 18, 53, 21, 23, 3, 81, 38, 14, 61, 7, 56, 31, 50, 44, 16, 17, 42, 57, 95, 55, 100, 78, 9, 68, 24, 75, 69, 96, 28, 84, 82, 2, 36, 94, 80, 15, 39, 99, 43, 25, 10, 87, 63, 41, 72, 65, 35, 12, 60, 33, 79, 90, 5, 51, 54, 74, 37, 40, 11, 93, 59, 98, 27, 49, 89, 83, 77, 86, 91, 97, 46, 1, 6, 76, 45, 73, 52, 88, 70, 13, 47, 85, 4, 34, 22, 20, 92, 62, 19, 64, 71, 66, 30, 26, 29, 58, 48, 67]
        res = quickSort(Hundred_list)                                                                                    
    delta = (datetime.now() - start)/10
    print("Quick sort took:         %s" %delta.total_seconds())
    print("Big O notation: Log linear O(n log n)\n")

    #Calculating the time taken for selection sort
    start = datetime.now()
    for i in range(10):
        Hundred_list = [8, 32, 18, 53, 21, 23, 3, 81, 38, 14, 61, 7, 56, 31, 50, 44, 16, 17, 42, 57, 95, 55, 100, 78, 9, 68, 24, 75, 69, 96, 28, 84, 82, 2, 36, 94, 80, 15, 39, 99, 43, 25, 10, 87, 63, 41, 72, 65, 35, 12, 60, 33, 79, 90, 5, 51, 54, 74, 37, 40, 11, 93, 59, 98, 27, 49, 89, 83, 77, 86, 91, 97, 46, 1, 6, 76, 45, 73, 52, 88, 70, 13, 47, 85, 4, 34, 22, 20, 92, 62, 19, 64, 71, 66, 30, 26, 29, 58, 48, 67]
        res = selectionSort(Hundred_list)                                                                                    
    delta = (datetime.now() - start)/10
    print("Selection sort took:     %s" %delta.total_seconds())
    print("Big O notation: Polynomial O(n^k)\n")


if __name__ == '__main__':
    sys.exit(main())
    