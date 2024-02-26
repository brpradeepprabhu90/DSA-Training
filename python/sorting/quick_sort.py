
# [5,3,1,4,6,2]
# [5,3,1,4,2,6]
# [2,3,1,4,5,6]

# [2,3,1,4] [6]
# [2,1,3,4]
# [1,2,3,4]

def swap(list, a,b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
def pivot(array,pivotIndex,endIndex):
    swapIndex= pivotIndex
    for i in range(pivotIndex + 1, endIndex +1):
        if(array[i]< array[pivotIndex]):
            swapIndex +=1
            swap(array,swapIndex,i)         
            
    swap(array,pivotIndex,swapIndex)
    return swapIndex


def quick_sort(array,start,endIndex):
    if(start < endIndex):
        pivotIndex =pivot(array,start,endIndex)
        quick_sort(array,start, pivotIndex -1)
        quick_sort(array,pivotIndex + 1,endIndex)
    return array


print(quick_sort([4,6,1,7,3,2,5],0,6))