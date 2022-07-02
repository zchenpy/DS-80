575. Distribute Candies
https://leetcode.com/problems/distribute-candies/

# set

class Solution:
  def distributeCandies(self, candyType: List[int]) -> int:
    return min(len(set(candyType)), len(candyType)//2)  
  
#Time complexity: O(n)
#Space complexity:O(n)  
