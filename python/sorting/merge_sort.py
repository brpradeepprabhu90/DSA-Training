
def merge(left,right):
    combined = []
    i=0
    j=0
    while i < len(left) and j < len(right):
        if(left[i]< right[j]):
            combined.append(left[i])
            i = i + 1
        else:
            combined.append(right[j])
            j= j + 1
    while i < len(left):
        combined.append(left[i])
        i= i + 1
    while j < len(right):
        combined.append(right[j])
        j = j + 1
    return combined

def mergeSort(array):
    if len(array) == 1:
        return array
    else:
        mid = int(len(array)/2)
        left = mergeSort(array[:mid])
        right = mergeSort(array[mid:])
        return merge(left,right)



list1 = [1,3,5,7]
list2 = [2,4,6,8]

print(mergeSort([3,5,2,1,7,6]))
    
        