intList = [5,3,1,4,6]



def selectionSort(array):
    for i in range(len(array)-1):
        minIndex = i
        for j in range(i+1,len(array)):
            if(array[minIndex]>array[j]):
                minIndex = j
        if(minIndex != i):
            temp = array[i]
            array[i] =array[minIndex]
            array[minIndex] = temp
    return array


print(selectionSort(intList))
