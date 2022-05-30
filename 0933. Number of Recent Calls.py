933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/
  
#1. Queue
class RecentCounter:

    def __init__(self):
        self.recentcounter=deque([])

    def ping(self, t: int) -> int:
        self.recentcounter.append(t)
        while t-self.recentcounter[0]>3000:
            self.recentcounter.popleft()
        return len(self.recentcounter)    
#Time complexity: O(n)
#Space complexity:O(n)


        
#2. Binary Search:
class RecentCounter(object):

    def __init__(self):
        self.request = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """            
        self.request.append(t)
        #print(self.request)
        #print(self.request[-1])
        
        l,r = -1, len(self.request)+1
        while l+1 != r:
            m = l+(r-l)//2
            if self.request[m] >= self.request[-1] -3000:
                r = m
            else:
                l = m
                
        return len(self.request) - r
      
#Time complexity: O(nlog(n))
#Space complexity:O(n)
