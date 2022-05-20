https://leetcode.com/problems/missing-number/

#1. Hashtable
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for number in range(len(nums)+1):
            if number not in set(nums):
                return number
              
#Time complexity: O(n)
#Space complexity:O(n)



#2. Math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_ap = n*(1+n)//2                    #Sum of Arithmetic Progression
        return sum_ap - sum(nums)
    
                  
#Time complexity: O(n)
#Space complexity:O(1)
