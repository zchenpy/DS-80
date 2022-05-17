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


#2. Queue
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
#Time complexity:  O(min(n,m))
#Space complexity: O(min(n,m)) 


#3.Stack
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q),]
        while stack:
            (check_p,check_q) = stack.pop()
            if not check_p and not check_q:
                continue
            elif check_p and check_q and check_p.val == check_q.val:
                stack.append((check_p.right,check_q.right))
                stack.append((check_p.left,check_q.left))
            else: return False
        return True   
#Time complexity:  O(min(n,m))
#Space complexity: O(min(n,m)) 
