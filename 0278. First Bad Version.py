278. First Bad Version
https://leetcode.com/problems/first-bad-version/
  
# Binary search 


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r  = 0, n+1
        while l+1 != r:
            m = l + (r-l)//2
            if isBadVersion(m):
                r = m
            else:
                l = m
        return r     

#Time complexity: O(logn)
#Space complexity:O(1)
