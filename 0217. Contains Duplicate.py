217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
  
  #1. Hashmap
  class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}
        for e in nums:
            if e in hashmap:return True
            else: hashmap[e] = ''     
        return False
      
#Time complexity: O(n)
#Space complexity:O(n)    
      
      
  #2.Hashmap/set
  class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(set(nums)) != len(nums)
      
#Time complexity: O(n)
#Space complexity:O(n)
