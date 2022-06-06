169. Majority Element
https://leetcode.com/problems/majority-element/

#1 
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
#Time complexity: O(nlogn)
#Space complexity:O(logn)
      
  
#2 Counter/Hashmap
class Solution(object):
  from collections import Counter
  def majorityElement(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      counter_nums = Counter(nums)
      for e in counter_nums:
          if counter_nums[e] > len(nums)//2:
              return e
#Time complexity: O(n)
#Space complexity:O(n)

  
