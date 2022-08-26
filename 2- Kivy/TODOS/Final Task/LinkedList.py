class Node:
    def __init__(self, *args):
        self.val = None
        self.next = None
        
        if len(args) >= 1:
            self.val = args[0]
    
        if len(args) == 2:
            self.next = args[1]
            
class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.count = 0
        
    def addFront(self, val):
        newNode = Node(val, self.head)
        self.head = newNode
        if not self.tail: 
            self.tail = newNode
        self.count += 1
        
    def removeFront(self):
        if self.count == 0:
            raise Exception("Empty Already")
        
    
    def print(self):
        temp = self.head
        while temp :
            print(temp.val, end=' ')
            temp = temp.next
            
myList = LinkedList()

myList.addFront(5)
myList.addFront(7)
myList.addFront(8) 

myList.print()