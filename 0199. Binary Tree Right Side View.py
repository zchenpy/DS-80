https://leetcode.com/problems/binary-tree-right-side-view/
  
# BFS-Queue  
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        queue = deque([root,])
        output = []
        while queue:
            n=len(queue)            
            for i in range (n):
                check = queue.popleft()                
                if i == n-1: output.append(check.val)
                if check.left: queue.append(check.left)
                if check.right: queue.append(check.right)
        return output  
      
#Time complexity: O(n)
#Space complexity:O(n)
