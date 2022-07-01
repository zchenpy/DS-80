367. Valid Perfect Square
https://leetcode.com/problems/valid-perfect-square/

#Binary Search  
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r=-1,num+1
        while l+1< r:
            m = l+(r-l)//2
            if m*m == num:
                return True
            elif m*m < num:
                l=m
            else:
                r=m
        return False   

#Time complexity: O(logn)
#Space complexity:O(1)
