844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/
  
#1. Stack
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
            stack_s = []
            stack_t = []
            
            for e in s:
                if e!= '#':
                    stack_s.append(e)
                else:
                    if stack_s:
                        stack_s.pop()
            for e in t:
                if e!= '#':
                    stack_t.append(e)
                else:
                    if stack_t:
                        stack_t.pop()
                        
            return stack_s == stack_t   
#Time complexity: O(m+n)
#Space complexity:O(m+n)          
          
