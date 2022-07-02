70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
  
#DP
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1: return 1
        if n == 2: return 2
        
        dp = [0]* n
        dp[0] = 1
        dp[1] = 2
        
        for i in range (2, n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]
#Time complexity: O(n)
#Space complexity:O(n)


----------------------------------------------------------    
#DP-Rolling Array
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        
        step1,step2 = 1,2
        
        for i in range (3,n+1):
            step3 = step1 + step2
            step1, step2 = step2, step3
        return step3    

#Time complexity: O(n)
#Space complexity:O(1)
