# Stack

class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(':')', '{': '}', '[' : ']'}
        stack = []
        
        for item in s:           
            if item in pair.keys():
                stack.append(item)               
            else:
                if not stack or item != pair[stack[-1]]:
                    return False
                stack.pop()               
        return not stack 

#Complexity O(n)
#Space complexity O(n)
