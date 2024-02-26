#5,3,1,4,6
#3,5,1,4,6
#1,3,5,4,6
#1,3,4,5,6

#6,5,4,3,2,1

#worst case (0(n**2))
#best case(O(n))
def insertionSort(array):
    for i in range(1, len(array)):
        temp =  array[i]
        j = i-1
        while temp < array[j] and j > -1:
            array[j+1] = array[j]
            array[j] =temp
            j-=1
    return array

print(insertionSort([5,3,1,4,6]))