#1 - Two Pointer

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l < r:
            if numbers[l]+numbers[r] == target:
                return[l+1,r+1]
            elif numbers[l]+numbers[r] < target:
                l+=1
            else:
                r-=1
 #Time Complexity: O(n)
 #Space Complexity O(1)
---------------------------------------------------------------------

#2 - Hashtable

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range (len(numbers)):
            if target - numbers[i] in hashtable:
                return[hashtable[target-numbers[i]]+1,i+1]
            else:
                hashtable[numbers[i]] = i
 #Time Complexity: O(n)
 #Space Complexity O(n)            
