852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/
  
#1. Binary search

class Solution:
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
      l,r  = 0, len(arr)-1
      while l+1 != r:
          m = l+(r-l)//2
          if arr[m-1]<=arr[m]:
              l=m
          else:
              r=m
      return l 
#Time complexity: O(log(n))
#Space complexity:O(1)    
    
  
  
#2. Max value
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))   
#Time complexity: O(n)*2
#Space complexity:O(1)         
