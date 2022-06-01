394. Decode String
https://leetcode.com/problems/decode-string/
  
 # stack1
class Solution:
    def decodeString(self, s: str) -> str: #  "32[a2[c]]"
        num = []
        letter = ['',]
        
        for e in s:
            if e.isnumeric():  
                if len(letter) != len(num): 
                    num.append(e)   
                else:
                    num[-1]+=e 
            
            if e=='[':
                letter.append('') 
                
            if e.isalpha():
                letter[-1]+=e 
            
            if e == ']':
                n = num.pop()
                string = letter.pop()
                letter[-1] += int(n)*string
                
        return letter[-1]       
            
#  "32[a2[c]]"
#1,num ['3',] letter['']              
#2,same layer  num['32'],letter['']              
#3, num['32'],letter['','']                
#4, num['32'],letter['','a']      
#5,num['32','2'],letter['','a']
#6,num['32','2'],letter['','a','']   
#7,num['32','2'],letter['','a','c'] 
#8, n = 2, string = c, letter[-1] = 'a'+2*'c'   -->>>num['32'], letter['','acc']
# 32*'acc'

#Time complexity: O(n)
#Space complexity:O(n)

# stack2
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for e in s:
            if e != ']':
                stack.append(e) 
            
            else: #e == ']'
                letter = ''
                while stack and stack[-1]!='[': 
                    letter = stack.pop()+letter
                    
                if stack[-1] == '[':
                    stack.pop()
                
                number = ''
                while stack and stack[-1].isnumeric():
                    number = stack.pop()+number
                    
                stack.append(int(number)*letter)
        
        return ''.join(stack) 
      
#Time complexity: O(n)
#Space complexity:O(n)
