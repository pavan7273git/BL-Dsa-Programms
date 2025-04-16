
class Queue:
    def __init__(self):
        self.queue=[]

    def enque(self,value):
        self.queue.append(value)

    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        """Displays the queue."""
        print("Queue:", self.queue)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()  

print(queue.dequeue())  
queue.display()  

print(queue.is_empty())  
print(queue.size())  
