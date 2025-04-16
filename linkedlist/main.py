from linkedlist import LinkedList

def main():
    ll=LinkedList()
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    print(f"List after inserting the elements")
    ll.display()
    ll.length()

    ll.insert_at_start(1)
    # ll.insert_at_start(2)
    # ll.insert_at_start(3)
    # ll.insert_at_start(4)
    # ll.insert_at_start(5)
    print(f'linked list after inserting at start')
    ll.display()
    ll.length()

    # ll.insert_at_specific(7,2)
    # print(f'Inserted at specific position')
    # ll.display()

    ll.insert_before(20,3)
    print('inserted before ')
    ll.display()

    ll.insert_after(32,4)
    print('inserted after ')
    ll.display()

    ll.delete_at_end()
    print(f'Linked list after deleting the last element')
    ll.display()

    ll.delete_at_start()
    print(f'Linked List after deleting the first element.')
    ll.display()

    ll.delete_at_position(1)
    ll.display()
    ll.length()

    #ll.insert_at_specific(7,4)

    ll.update_at_first(79)
    ll.display()

    ll.update_at_last(99)
    ll.display()
    
    ll.update_data(3,19)
    ll.display()

    ll.get_first()
    ll.get_last()
    ll.get_element_at_position(1)

    ll.reverse()
    ll.display()

if __name__ == "__main__":
    main()