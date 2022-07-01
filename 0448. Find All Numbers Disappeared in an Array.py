448. Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

 #1. Hashmap
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        res = []
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                res.append(i)
        return res        
#Time complexity: O(n)
#Space complexity:O(n)    



#2 
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
            
        return [i+1 for i, n in enumerate(nums) if nums[i] >0]
      
#Time complexity: O(n)
#Space complexity:O(n)      
      
