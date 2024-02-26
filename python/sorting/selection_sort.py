
#5,3,1,4,6
#1,3,5,4,6
#1,3,4,5,6

def swap(list, a,b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
    
## O(n**2)
def selection_sort(array):
    for i in range(len(array)-1):
        minIndex = i
        for j in range(i+1, len(array)):
            if(array[minIndex] > array[j]):
                minIndex = j  
        if(i!= minIndex):              
            swap(array,i, minIndex)
    return array 






print(selection_sort([5,3,1,4,6]))