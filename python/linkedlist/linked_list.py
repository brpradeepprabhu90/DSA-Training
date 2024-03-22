class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
# Append- O(1)
# Prepend - O(1)
# Pop - O(N)
# PopFirst - O(1)
# Get - O(N)
# Set - O(N)
class LinkedList:
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
            self.tail = newNode
        self.length +=1
        return True
    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            prev = self.head
            while (temp.next):
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
            self.length -=1
            if self.length == 0: 
                self.head = None
                self.tail = None
            return temp
        
    def prepend(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length +=1
        return True
        
    def popFirst(self):
        if self.length == 0:
            return None
        temp =self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length == 0: 
                self.head = None
                self.tail = None
        return temp
    
    def getValue(self,index):
        if index <0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
