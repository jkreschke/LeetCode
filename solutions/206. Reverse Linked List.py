# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Two pointer solution. O(n) time, O(1) space
        '''
        if not head or not head.next:
            return head
        newHead = head
        while head.next:
            p = head.next
            head.next = p.next
            p.next = newHead
            newHead = p
        
        return newHead
    
        '''
        Recursive solution O(n) time, O(n) space from recursive call stack
        '''
        def helper(node):
            if not node: return None, None
            if not node.next: return node,node
            new_head,tail = helper(node.next)
            node.next = None
            tail.next = node
            return new_head, node
        
        new_head, _ = helper(head)
        return new_head
                
