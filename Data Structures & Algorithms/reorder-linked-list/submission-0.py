# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next # these are pointers being initialised

        second=slow.next
        slow.next=prev=None
        while second:
            temp=second.next # thsi code clock is for reversing
            second.next=prev
            prev=second
            second=temp
        
        first,second=head,prev
        while second:
            temp1,temp2=first.next,second.next
            first.next=second # for merging
            second.next=temp1
            first=temp1
            second=temp2