https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#1. DP  
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dp[i][0] - day i: no stock in hand( no stock day[i-1][0], or hold stock day[i-1][1], sold day i )
        dp[i][1] - dayi: hold sotck(hold stock day[i-1][i], no stock in day[i-1][0] buy stock day i)
        '''
        #corner condition
        if n == 0: return 0
        
        #create dp array
        n = len(prices)
        dp = [[0]*2 for x in range(n)]
        
        # dp initiation
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] =max(dp[i-1][1],dp[i-1][0]-prices[i])
        return max(dp[-1])   

#Time complexity: O(n)
#Space complexity:O(n)
            
