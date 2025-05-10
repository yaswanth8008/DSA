# https://leetcode.com/problems/reverse-linked-list/submissions/1629905510/


def reverseList(head):
    h1 = head
    h2 = None
    while h1 != None:
        temp = h1
        h1 = h1.next
        temp.next = h2 
        h2 = temp 
    return h2