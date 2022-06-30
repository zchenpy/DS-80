922. Sort Array By Parity II
https://leetcode.com/problems/sort-array-by-parity-ii/
  
#Two pointers

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        while even <= len(nums)-1 and odd <= len(nums)-1:
            if nums[even] %2 == 0:
                even += 2
            else:
                if nums[odd] %2 == 0:
                    nums[even], nums[odd] = nums[odd], nums[even]
                odd += 2                
        return nums    
      
#Time complexity: O(n)
#Space complexity:O(1)
