515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/

#1.  BFS-Queue

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        queue = deque([root,])
        output = []
        while queue:
            n = len(queue)
            max_of_layer = -float(inf)
            for i in range(n):
                check = queue.popleft()
                max_of_layer = max(max_of_layer,check.val)
                if check.right:
                    queue.append(check.right)
                if check.left:
                    queue.append(check.left)
            output.append(max_of_layer)
        return output 
      
#Time complexity: O(n)
#Space complexity:O(n)     

