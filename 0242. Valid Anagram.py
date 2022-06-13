242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

# Hashmap/Counter  
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
      
#Time complexity: O(n)
#Space complexity:O(n) 
