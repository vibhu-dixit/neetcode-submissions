# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next
        NextNode = None
        tail = curr 
        
        prev_sub = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev_sub
            prev_sub = curr
            curr = nxt
        
        NextNode = curr
        prev.next = prev_sub
        tail.next = NextNode

        return dummy.next
