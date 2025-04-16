from collections import deque

class Stack:
    def __init__(self):
        self.stack=deque()

    def push(self,data):
        self.stack.append(data)

    def size_of_satck(self):
        return len(self.stack)
    
    def isEmpty(self):
        return len(self.stack)==0
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return 'Stack is Empty'
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return 'Stack is Empty'
    
    def search(self,target):
        if  self.isEmpty():
            print('The Stack is Empty.')
            return
        
        if target in self.stack:
            print('The Element is in stack.')
            return
        
    def element_at_position(self,position):
        if self.isEmpty():
            print('Stack is Empty.')
            return
        
        if position> len(self.stack)-1:
            print('The Position is Out of Bound')
            return
        
        print(f'The Element at position is: {self.stack[position-1]}')

    def print_all_elements(self):
        print(f'The stack is: {list(reversed(self.stack))}')



sd=Stack()
sd.push(45)
sd.push(33)
sd.push(21)
sd.push(56)
print(sd.size_of_satck())

sd.print_all_elements()

sd.element_at_position(3)

sd.search(32)

print(sd.pop())
print(sd.peek())   

    