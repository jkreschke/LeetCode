"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
​
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        O(n) time, O(1) space
        '''
        if not root: return root
        root.next = None
        cur = root
        while cur.left:
            scan = cur
            scan.left.next = scan.right
            while scan.next:
                scan.right.next = scan.next.left
                scan = scan.next
                scan.left.next = scan.right
            cur = cur.left
        return root
                
            
        
        
