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
