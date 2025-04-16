'''Stacks Implementation using Stacks.'''

class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)

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
    
    def size_stack(self):
        return len(self.stack)
    
    def print_stack(self):
        print("stack is ",self.stack[::-1])

    def element_at_position(self,position):

        if position>len(self.stack)-1:
            print('The Position is Out of Bound')
            return
        
        print(f'The Element in the Stack at position is : {self.stack[position]}')
        return
    
    def clear_stack(self):
        self.stack.clear()


    def search(self,target):
        if self.isEmpty():
            print('The List is Empty.')
            return
        
        if target in self.stack:
            print(f'The Element is in Stack.')
            return
        else:
            print('The Element is not in stack.')
    

sl=Stack()
sl.push(21)
sl.push(34)
sl.push(43)
sl.push(12)

sl.print_stack()

print(sl.pop())
print(sl.pop())

print(sl.peek())
print(sl.isEmpty())
print(sl.size_stack())
sl.print_stack()
sl.element_at_position(2)
sl.search(12)
sl.clear_stack()
sl.print_stack()

