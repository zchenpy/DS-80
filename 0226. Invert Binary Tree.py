https://leetcode.com/problems/invert-binary-tree/
#Recursion
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
#Time complexity: O(n)
#Space complexity:O(n)
