# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Fast and slow pointer, one pass. O(n) time, O(1) space
        '''
        fast = slow = head
        while True:
            if not fast or not fast.next:
                return slow
            slow = slow.next
            fast = fast.next.next
            
        
