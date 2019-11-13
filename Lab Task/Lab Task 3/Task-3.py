def selectionSort(a):
    for i in (0, len(a)-1):
        min = i
        b = i+1
        for j in range(b, len(a)):
            if a[j] < a[min]:
                min = j
        if min != i:
            a[i] = c
            a[i] = a[min]
            a[min] = c
    return a

a = [1,5,2,3]

print(selectionSort(a))
