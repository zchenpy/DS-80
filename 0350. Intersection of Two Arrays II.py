350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
  
#1. Hashtable/Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return (Counter(nums1)&Counter(nums2)).elements()
      
#Time complexity: O(n)
#Space complexity:O(n)      
