# 1. DP
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [0]*n    
        
        dp[0] = nums[0] 
        for i in range(1,n):
            dp[i] = dp[i-1]+nums[i]
            
        return dp
#Time Complexity: O(n)
#Space Complexity: O(n)

----------------------------------------------------
# 2. One pointer. Inplace modification

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums

#Time Complexity: O(n)
#Space Complexity: O(1)
