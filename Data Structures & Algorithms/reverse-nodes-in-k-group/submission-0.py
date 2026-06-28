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
            kth = group_prev # 1. Find the kth node
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next   # not enough nodes left

            group_next = kth.next

            start = group_prev.next             # 2. Reverse the group
            new_head = self.reverse(start, group_next)

            group_prev.next = new_head            # 3. Reconnect
            start.next = group_next

            group_prev = start # 4. Move to next group

    def reverse(self,start,end):
        curr=start
        prev=None
        while curr != end:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        return prev
