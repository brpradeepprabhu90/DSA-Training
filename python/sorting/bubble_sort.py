intList = [5,3,1,4,6]



def bubbleSort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if(array[j]> array[j+1]):
                temp = array[j]
                array[j]= array[j+1]
                array[j+1] = temp
    return array


print(bubbleSort(intList))
