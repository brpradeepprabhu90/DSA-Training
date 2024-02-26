def merge(left,right):
    i=0
    j=0
    result = []
    while( i < len(left) and j < len(right)):
        if(left[i]< right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i+=1
    while (j < len(right)):
        result.append(right[j])
        j+=1
    return result


# O(n) = n log n
def mergeSort (array):
     if(len(array) == 1):
      return array
     else:
        mid = int(len(array)/2)
        left = mergeSort(array[:mid])
        right = mergeSort(array[mid:])
     return merge(left,right)

 
# [5,3,1,4,6,8,7,9]

# [5,3,1,4] [6,8,7,9]

# [5,3] [1,4] [6,8] [7,9]

# [5] [3] [1] [4] [6] [8] [7] [9]

# [3,5] [1,4] [6,8] [7,9]

# [1,3,4,5] [6,7,8,9]

# [1,3,4,5,6,7,8,9]

print(mergeSort([5,3,1,4,6]))