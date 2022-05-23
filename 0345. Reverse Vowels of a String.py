345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
  
#1. two pointers
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}
        list_s = list(s)
        l,r = 0, len(s)-1
        while l < r:
            if list_s[l] not in vowel:
                l+=1
            if list_s[r] not in vowel:
                r-=1
            if list_s[l] in vowel and list_s[r] in vowel:
                list_s[l], list_s[r] = list_s[r],list_s[l]
                l+=1
                r-=1
        return ''.join(list_s) 
#Time complexity: O(n)
#Space complexity:O(1)      
      
