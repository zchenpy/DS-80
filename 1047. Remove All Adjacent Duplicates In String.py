1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for e in s:
            if stack and stack[-1] == e:
                stack.pop()
            else:
                stack.append(e)
        return ''.join(stack)    
      
#Time complexity: O(n)
#Space complexity:O(1)      
