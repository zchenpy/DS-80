438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/
  
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        res=[]
        counter_sw = Counter(s[0:n])
        counter_p = Counter(p)
        
        for i in range(len(s)-n+1):
            if counter_sw == counter_p:
                res.append(i)
            counter_sw[s[i]] -= 1 #remove 1st letter in sliding window
            if i < len(s)-n:
                counter_sw[s[i+n]] += 1  #add one letter in slidding window
        return res
      
#Time complexity: O(n)
#Space complexity:O(n)      
