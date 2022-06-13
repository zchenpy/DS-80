389. Find the Difference
https://leetcode.com/problems/find-the-difference/submissions/


#Hashtable/Counter
class Solution:
    from collections import Counter
    def findTheDifference(self, s: str, t: str) -> str:
        return list((Counter(t)-Counter(s)).keys())[0]
      
#Time complexity: O(m+n)
#Space complexity:O(m+n)      
