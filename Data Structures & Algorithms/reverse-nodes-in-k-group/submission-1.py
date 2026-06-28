# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth=group_prev
            for _ in range(k):
                kth=kth.next
                if not kth:
                    return dummy.next
            start=group_prev.next
            group_next=kth.next
            new_head=self.reverse(start,group_next)
            group_prev.next=new_head
            start.next=group_next

            group_prev=start

    def reverse(self,start,end):
        curr=start
        prev=None
        while curr != end:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        return prev
