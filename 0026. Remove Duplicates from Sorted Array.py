#1. Two pointer, modification in place

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(0,len(nums)):
            if nums[r]!= nums[l]:
                nums[l+1],nums[r] = nums[r],nums[l+1]
                l+=1    
        return l+1
      
#Time complexity: O(n)
#Space complexity:O(1)
