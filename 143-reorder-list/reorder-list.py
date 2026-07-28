# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        second=slow.next
        slow.next=None
        prev=None
        while second:
            n=second.next
            second.next=prev
            prev=second
            second=n
        second=prev
        first=head
        while second:
            d1=first.next
            d2=second.next
            first.next=second
            second.next=d1
            first=d1
            second=d2