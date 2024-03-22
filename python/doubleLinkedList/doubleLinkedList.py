class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
# Append- O(1)
# Prepend - O(1)
# Pop - O(1)
# PopFirst - O(1)
# Get - O(N)
# Set - O(N)
class DoubleLinkedList:
    def __init__(self,value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length +=1
        return True
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next =None
        self.length -=1
        return temp
        
    def prepend(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length +=1
        return True
        
    def popFirst(self):
        if self.length == 0:
            return None
        temp =self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.length -=1
       
        return temp
    
    def getValue(self,index):
        if index <0 or index > self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
             temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
    
    def setValue(self,index,value):
        temp = self.getValue(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index, value):
        if index <0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newNode = Node(value)
        temp = self.getValue(index - 1)
        newNode.next = temp.next
        temp.next = newNode
        self.length +=1
        return True
    
    def remove(self,index):
        if index <0 or index > self.length:
            return None
        if index == 0:
            self.popFirst();
        if index == self.length:
            return self.pop()
        prev = self.getValue(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp
        
list = LinkedList(12)
list.append(13)
list.append(14)
list.printList()
print("Removed",list.pop())
print("Removed",list.pop())
list.prepend(11)
list.prepend(10)
list.printList()
print("--------Poping Items------------")
list.popFirst()
list.printList()
print("--------Getting values------------")
print(list.getValue(1).value)

print("--------Setting values------------")
list.setValue(1,14)

list.append(15)
list.append(16)

print(list.printList())
print("--------Inserting values------------")
list.insert(1,12)
print(list.printList())
print("--------Remvoing values------------")
list.remove(2)
print(list.printList())
