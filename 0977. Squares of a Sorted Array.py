977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
  
#Two pointers  

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        i, j = 0, len(nums)-1
        for p in range(len(nums)-1, -1, -1):
            if abs(nums[i]) >= abs(nums[j]):
                res[p] = nums[i]*nums[i]
                i += 1
            else:
                res[p] = nums[j]*nums[j]
                j -= 1
        return res         
      
#Time complexity: O(n)
#Space complexity:O(n)
