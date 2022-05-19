https://leetcode.com/problems/find-smallest-letter-greater-than-target/
##1. Binary search 

  class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1]:
            return letters[0]
        else:
            l,r = -1 , len(letters)
            while l+1!=r:
                m = l+(r-l)//2
                if letters[m] <= target:
                    l = m
                else:
                    r = m
            return letters[r]        

#Time complexity: O(nlogn)
#Space complexity:O(1)
