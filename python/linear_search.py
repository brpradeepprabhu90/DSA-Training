list = ["python","c++","javascript","testing"]


def linearSearch(array, find):
    for idx,el in enumerate(array):
        if el == find:
            return idx
    return -1    


print(linearSearch(list,"javascript"))

print(linearSearch(list,"pradeep"))



