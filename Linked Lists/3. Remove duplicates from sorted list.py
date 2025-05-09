# Given a sorted linked list, delete all duplicates such that each element appears only once.

	
def deleteDuplicates(A):
    tmp = A
    while tmp!=None and tmp.next!=None:
        if tmp.val == tmp.next.val:
            tmp.next = tmp.next.next 
        else:
            tmp = tmp.next
            
    return A