442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/
  
#1. inplace   
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
#range of nums : 1 ~ n
#range of index: 0 ~ n-1
        res = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                res.append(abs(n))
            nums[abs(n)-1] *= -1
        return res    
        
#time complexity: O(n)
#space complexity: O(1)  



#2 Counters/Hashmap
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return list((Counter(nums) - Counter(set(nums))).keys())
#time complexity: O(n)
#space complexity: O(n)  




#3. Counters/Hashmap
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:      
        counter_nums = Counter(nums)      
        res = []
        for n in counter_nums:
            if counter_nums[n] > 1:
                res.append(n)       
        return res 
      
#time complexity: O(n)
#space complexity: O(n) 
