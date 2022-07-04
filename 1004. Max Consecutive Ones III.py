1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/
  
# Two Pointers  
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        zero_num = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_num += 1
            while zero_num > k:
                if nums[l] == 0:
                    zero_num -= 1
                l += 1            
            res = max(res, r-l+1)        
        return res 
#Time complexity: O(n)
#Space complexity:O(1)      
