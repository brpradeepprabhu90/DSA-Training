# [5,3,1,4,6]
# [3,1,4,5,6]
# [1,3,4,5,6]

#O(n**2)

def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if (array[j]> array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

print(bubble_sort([5,3,1,4,6]))