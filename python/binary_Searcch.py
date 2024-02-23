import math
intList = [1,4,8,12,14,16,133]
find  = 6


def binarySearch(array, find):
    mid = math.floor(len(array)/2)
    if mid == 0 and array[mid] != find:
        return "not found"
    elif(array[mid] == find):
        return "value find"
    elif (array[mid]  > find):
        return binarySearch(array[0:mid-1],find)
    elif (array[mid]  < find):
        return binarySearch(array[mid:len(array)],find)
    return "not found"

def binarySearchIndex(array,left,right,find):
    if right >= left:
        mid = math.floor((left + right)/2)
        if array[mid] == find:
            return mid
        elif array[mid] > find:
            return binarySearchIndex(array,left,mid-1,find)
        else:
            return binarySearchIndex(array,mid + 1, right, find)
    else:
        return -1
print(binarySearch(intList, find))
print(binarySearchIndex(intList, 0, len(intList)-1,find))