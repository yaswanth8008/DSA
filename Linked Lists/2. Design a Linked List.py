# Design and implement a Linked List data structure.
# A node in a linked list should have the following attributes - an integer value and a pointer to the next node.

# It should support the following operations:

# insert_node(position, value) - To insert the input value at the given position in the linked list.
# delete_node(position) - Delete the value at the given position from the linked list.
# print_ll() - Print the entire linked list, such that each element is followed by a single space (no trailing spaces).


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = None
size = 0

def insert_node(position, value):
   
    global head
    global size
   
    if position > size + 1:
        # bad index
        return
   
    n = Node(value)
    if position == 1:
        n.next = head
        head = n
    else:
        temp = head
        for i in range(1, position-1):
            temp = temp.next
   
        n.next = temp.next
        temp.next = n
       
    size += 1

def delete_node(position):
   
    global head
    global size
   
    if position > size:
        # bad index
        return

    if position == 1:
        head = head.next
    else:
        temp = head
        for i in range(1, position-1):
            temp = temp.next
       
        temp.next = temp.next.next
       
    size -= 1

def print_ll():
    global head
    global size
   
    if size == 0:
        return
    printVal = head
    while printVal.next != None:
        print(printVal.data, end=" ")
        printVal = printVal.next
    print(printVal.data)
