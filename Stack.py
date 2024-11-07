class Stack:
    def __init__(self) -> None:
        self.topValue : Nodo = None
    
    def empty(self):
        return self.topValue == None
    
    def push(self,value):
        
        node = Nodo(value)
        node.next = self.topValue
        self.topValue = node
        
    def pop(self):
        poppedValue = self.topValue.value
        self.topValue = self.topValue.next
        return poppedValue
    
    def size(self):
        
        if self.empty():
            return 0
        
        node = self.topValue
        size = 1
        while node.next != None:
            size += 1
            node = node.next
            
        return size
    

class Nodo:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None