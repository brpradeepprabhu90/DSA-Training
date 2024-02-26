#O(1)
def printConstantTime(n):
    return n + n * n  + n
#O(n)
def printItems(n):
    for i in range(n):
        print(i)

#0(n*2)
def printMultipleItems(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

#0(n + n)=> O(2n) => O(n)
def printIndivdualloops(n):
    for i in range(n):      
        print(i)
    for j in range(n):
        print(j)

#O((n * 2) + O(n)  ) => O(n*2)
def printDoublingloops(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for i in range(n):      
        print(i)


# [1,2,3,4,5,6,7,8]
# [5,6,7,8]
# [7,8]
# [7]
# 2**3 = 8
# log2 8 = 3 
# (log n)
        
def printDivideAndConquerer(array,left,right,find):
    if right >= left:
        mid = left + right // 2
        if array[mid] == find:
            return mid
        elif array[mid] > find:
            return printDivideAndConquerer(array,left,mid-1,find)
        else:
            return printDivideAndConquerer(array,mid + 1, right, find)
    else:
        return -1

printItems(10)