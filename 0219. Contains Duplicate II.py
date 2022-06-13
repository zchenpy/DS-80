219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/
  
#1. Hashmap
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        for i in range (len(nums)):
            if nums[i] in hashmap and i - hashmap[nums[i]]<=k:
                return True
            hashmap[nums[i]] = i
        return False   
#Time complexity: O(n)
#Space complexity:O(n)      
      

  
#2 Sliding window
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()
        pointer = 0
        for i in range(len(nums)):
            if i-pointer > k:
                seen.remove(nums[pointer])
                pointer += 1
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False  
      
#Time complexity: O(n)
#Space complexity:O(n)  
