https://leetcode.com/problems/valid-palindrome/
  
#Two pointers

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j = 0, len(s)-1
        while i < j:   
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1            
        return True    
      
#Time complexity: O(n)
#Space complexity:O(1)     
      
