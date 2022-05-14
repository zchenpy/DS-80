#1 DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])#max（rob house[i-2]+current hous[i]， rob house[i-1]+not rob current hous[i]）
        return dp[-1]   
      
#Time complexity: O(n)
#Space complexity:O(n)
--------------------------------------------------------------------------------------------------------


#2 DP - Rolling array
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        dp0 = nums[0]
        dp1 = max(nums[0],nums[1])
        
        for i in range(2,n):
            dp2 = max(dp1,dp0+nums[i])
            dp0,dp1 = dp1,dp2
        
        return dp2
#Time complexity: O(n)
#Space complexity:O(1), only record dp2
