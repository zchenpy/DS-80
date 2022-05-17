https://leetcode.com/problems/same-tree/
    
#1. Recursion:
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

#Time complexity:  O(min(n,m))
#Space complexity: O(min(n,m)) for extra stack space in recursion

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p,q),])       
        while queue:
            (p,q)=queue.popleft()
            if not p and not q:
                continue
            elif p and q and p.val==q.val:
                queue.append((p.left,q.left))
                queue.append((p.right,q.right))
            else: return False
        return True    
                
