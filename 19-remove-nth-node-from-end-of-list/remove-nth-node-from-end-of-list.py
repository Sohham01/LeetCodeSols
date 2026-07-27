# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res=ListNode(0,head)
        d1=res
        d2=head
        for _ in range(n):
            d2=d2.next
        while d2:
            d2=d2.next
            d1=d1.next
        d1.next=d1.next.next
        return res.next