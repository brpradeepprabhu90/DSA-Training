def swap(array,index1,index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def pivot(array,pivotIndex, endIndex):
    swap_index=pivotIndex
    for i in range(pivotIndex + 1, endIndex + 1):
        if array[i] < array[pivotIndex]:
            swap_index+=1
            swap(array,swap_index,i)
    swap(array,pivotIndex,swap_index)
    return swap_index



def quickSort(array,left,right):
    if left < right:
        pivotIndex = pivot(array,left,right)
        quickSort(array,left,pivotIndex -1)
        quickSort(array,pivotIndex+1,right)
    return array

print(quickSort([4,6,1,7,3,2,5],0,6))

        
