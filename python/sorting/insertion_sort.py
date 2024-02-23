
intList = [5,3,1,4,6]

def insertionSort(array):
    for i in range(1,len(array)):
       temp= array[i]
       j=i-1
       while temp < array[j] and j > -1:
           array[j+1] = array[j]
           array[j] = temp
           j-=1
        
    return array


print(insertionSort(intList))
