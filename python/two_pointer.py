import math;
list = ["python","c++","javascript","testing"]


def twoPointerSearch(array, find):
    length = len(array)
    for idx in range(math.ceil(length/2)):
        if array[idx] == find:
            return idx
        elif array[length-1-idx] == find:
            return array[length-1-idx]
    return -1    


print(twoPointerSearch(list,"javascript"))

print(twoPointerSearch(list,"pradeep"))
