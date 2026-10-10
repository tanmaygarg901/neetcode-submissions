# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        l = start
        right = head
        for i in range(n):
            right = right.next
        while right:
            l = l.next
            right = right.next
        l.next = l.next.next
        return start.next