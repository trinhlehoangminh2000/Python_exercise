def heap_sort(a, count):
    heapify(a, count)
    end = len(a)-1
    while end >0 :
        a[end] = k
        a[end] = a[0]
        a[0] = k
        end -= 1
        sift_down(a,0,end)

def heapify(a, count):
    start = floor((count-2)/2)
    while (start>= 0) :
        sift_down(a, start, count-1)
        start -=1

def sift_down(a, start, end):
    root = start
    while (root*2+1)<= end:
        swap = root
        child = root*2+1
        if a[swap]< a[child]:
            swap = child
        if ((child +1) <= end) and (a[swap] < a[child+1]):
            swap = child +1
        if swap != root:
            a[root] = k
            a[root] = a[swap]
            a[swap] = k
            root = swap
        else:
            return

a = [3,5,7,8,9,1,2]

print(heap_sort(a,7))
