https://leetcode.com/problems/move-zeroes/
Two pointers:

  class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range (len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums   
      
#Time complexity: O(n)
#Space complexity:O(1)
