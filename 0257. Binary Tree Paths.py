#1 DFS-Recursion

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

#Time complexity: O(n2)
#Space complexity:O(n2)
#Worst case: linked node. Path will be recorded for each node. Tree structure: nlog(n)


#2 DFS-Stack
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        output = []
        stack = [(root,''),]
        while stack:
            check,path = stack.pop()
            if not check.left and not check.right:
                output.append(path + str(check.val))
            
            if check.right:                                            #push child into stack，record current path
                stack.append((check.right, path+str(check.val)+'->'))  #tuple，(())
            if check.left:
                stack.append((check.left, path+str(check.val)+'->'))
        return output
    
#Time complexity: O(n2)
#Space complexity:O(n2)
