# Recursion

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []                                            #create list to do result storage - global variable
        current_path = ''                                      #create a string to record current path
        self.dfs(root,output,current_path)
        return output
    
    def dfs(self, root,output,current_path):
        current_path += str(root.val)
        if not root.left and not root.right:                   #if go to a leaf, append the path to output
            output.append(current_path)
            return
        if root.left:                                          #if root.left, update current_path
            self.dfs(root.left,output,current_path+'->')
        if root.right:                                         #if root.right, update current_path
            self.dfs(root.right,output,current_path+'->')

#Time complexity: O(n)
#Space complexity:O(n)
