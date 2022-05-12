# 1 hashtable

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashtable ={}
        for e in nums:
            hashtable[e] = hashtable.get(e,0) +1 
           
        for key in hashtable: 
            if hashtable[key]==1:
                return key
#Time Complexity:O(n)
#Space Complexity:O(n)

-------------------------------------------------------------
# 2 list and set
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)

#Time Complexity:2*O(n)
#Space Complexity:O(n)
      
      
      
