class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None 

    def insert_at_start(self, data):
        if self.isEmpty():
            newnode = Node(data)
            return
        newnode=Node(data) 
        newnode.next = self.head
        self.head = newnode

    def insert_at_end(self, data):
        newnode = Node(data)

        if self.isEmpty():
            self.head = newnode
            return

        temp = self.head
        while temp.next:  
            temp = temp.next
        temp.next = newnode  

    


    def insert_before(self,data,value):

        if self.isEmpty():
            print('List is Empty.')
            return
        
        if self.head.data==value:
            self.insert_at_start(data)
            return
        
        temp=self.head
        prev=None

        while temp and temp.data!=value:
            prev=temp
            temp=temp.next

        if temp is None:
            print(f'{value} is not found ')
            return
        
        newnode=Node(data)
        prev.next=newnode
        newnode.next=temp


    def insert_after(self,data,value):

        if self.isEmpty():
            print('List is Empty.')
            return
        
        
        
        temp=self.head
        while temp and temp.data!=value:
            temp=temp.next

        if temp is None:
            print(f'{value} is not found ')
            return
        
        newnode=Node(data)
        newnode.next=temp.next
        temp.next=newnode

    def delete_at_start(self):
        if self.isEmpty():
            print('List is Empty')
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.isEmpty():
            print("List is Empty")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next and temp.next.next:  # Fix: Stop one node before last
            temp = temp.next
        temp.next = None

    def delete_at_position(self, position):
        if self.isEmpty():  # Fix: Stop execution if empty
            print("List is Empty")
            return

        if position == 0:
            self.delete_at_start()
            return

        temp = self.head
        prev = None
        count = 0

        while temp and count < position:
            prev = temp
            temp = temp.next
            count += 1

        if temp is None:
            print(f'Invalid Position, Length Exceeded.')
            return

        prev.next = temp.next  # Properly unlink the node

    def length(self):
        count=0

        temp=self.head
        while temp:
            count+=1
            temp=temp.next

        print(f'The length of the list is: {count}')

    def update_at_first(self,data):
        if self.isEmpty():
            print('List is Empty.')
            return
        
        self.head.data=data

    def update_at_last(self,data):
        if self.isEmpty():
            print('List is Empty.')
            return
        
        temp=self.head
        while temp:
            if temp.next==None:
                temp.data=data
                return
            
            temp=temp.next






    def update_data(self,target,value):
        if self.isEmpty():
            print(f'List is Empty!.')
            return
    
        temp=self.head
        while temp:
            if temp.data== target:
                temp.data=value
                return

            temp=temp.next
            
    def get_first(self):
        if self.isEmpty():
            print('List is Empty.')
            return
        
        print(f'The data of first is:{self.head.data}')

    def get_last(self):
        if self.isEmpty():
            print('List is Empty.')
            return
        
        temp=self.head

        while temp:
            if temp.next==None:
                print(f'The last element data is:{temp.data}')
                return
            temp=temp.next


    def get_element_at_position(self,position):
        temp=self.head
        prev=None
        count=0

        while temp and count<position:
            prev=temp
            temp=temp.next
            count+=1

        if temp is None:
            print(f'Invalid Position, Length Exceeded.')
            return   

        print(f'The Element at position  is : {temp.data}')


    def reverse(self):
        if self.isEmpty():
            print('List is Empty.')
            return
        
        curr=self.head
        prev=None

        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next

        self.head=prev

    def display(self):
        if self.isEmpty():  
            print("List is Empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


