class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root = TreeNode()
        if not root1 and not root2:
            return 
        elif root1 and not root2:
            root = root1
        elif not root1 and root2:
            root = root2
        else:
            root.val = root1.val+root2.val
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
        return root 
      
#Time complexity: O(min(m,n)) , m:node number of root1, n: node number of root2
#Space complexity:O(min(m,n))
