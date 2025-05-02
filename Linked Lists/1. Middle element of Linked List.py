# Given a linked list of integers, find and return the middle element of the linked list.



# NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.



# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        temp = A 
        cnt = 1
        while temp.next != None:
            cnt += 1
            temp = temp.next 
        index = (cnt//2) + 1
        temp = A 
        i = 1
        while i < index:
            temp = temp.next 
            i += 1 
        return temp.val