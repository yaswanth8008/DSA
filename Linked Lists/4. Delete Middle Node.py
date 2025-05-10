# Given a singly linked list, delete middle of the linked list.

# For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5

# If there are even nodes, then there would be two middle nodes, we need to delete the second middle element.

# For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.

# Return the head of the linked list after removing the middle node.

# If the input linked list has 1 node, then this node should be deleted and a null node should be returned.


def solve(A):
    temp = A 
    size = 0
    while temp != None:
        size += 1
        temp = temp.next 
    if size <= 1:
        return None
    k = (size//2) 
    
    temp = A
    i = 1
    while i < k:
        i += 1
        temp = temp.next
    temp.next = temp.next.next
    return A