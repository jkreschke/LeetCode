# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Two pointer solution. O(n) time, O(1) space
        '''
        fast = head
        for _ in range(n):
            fast = fast.next
        cur = head
        while fast:
            prev = cur
            fast = fast.next
            cur = cur.next
        if cur == head:
            return head.next
        prev.next = cur.next
        return head
        
