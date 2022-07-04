1441. Build an Array With Stack Operations
https://leetcode.com/problems/build-an-array-with-stack-operations/
  
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        p = 0
        res = []
        for i in range(1,target[-1]+1):
            res.append('Push')
            if i != target[p]:
                res.append('Pop')
            else:
                p += 1
        return res
#Time complexity: O(n)
#Space complexity:O(n)      
