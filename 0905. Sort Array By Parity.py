905. Sort Array By Parity
https://leetcode.com/submissions/detail/677042399/
  
# Two pointers -1 

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        s=0
        for f in range(len(nums)):
            if nums[f] %2 ==0:
                nums[s],nums[f] =nums[f],nums[s] 
                s+=1
        return nums  
      
      
# Two pointers -2 
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:        
      i, j = 0, len(nums)-1
          while i < j:
              if nums[i]%2 != 0:
                  if nums[j]%2 == 0:
                      nums[i], nums[j]= nums[j],nums[i]
                  else:
                      j-=1
              else:
                  i+=1
          return nums 
#Time complexity: O(n)
#Space complexity:O(1)
