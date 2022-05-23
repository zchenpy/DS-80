https://leetcode.com/problems/intersection-of-two-arrays/
  
  #1. Counters
  class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return (Counter(nums1)&Counter(nums2)).keys()
 
#Time complexity: O(m+n)
#Space complexity:O(m+n)
