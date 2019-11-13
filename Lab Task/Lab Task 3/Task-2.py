arr = [1,2,3,4,5,6,7]
tar = 1

def linearSearchIt(arr, tar):
    check = False
    for i in range (0, len(arr)):
        if (arr[i] == tar):
            check = True
            break
    if check == True :
        return("Found!")
    else:
        return("Not found!")

def linearSearchRe(arr, tar):
    if arr == [] :
        return "Not Found!"
    if arr[len(arr)-1] == tar:
        return "Found!"
    else:
        arr.pop()
        return linearSearchRe(arr, tar)
print(linearSearchIt(arr, tar))
print(linearSearchRe(arr, tar))
