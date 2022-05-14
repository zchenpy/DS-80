# Stack
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score_stack = []
        for e in ops:
            if e == 'D' and score_stack:
                score_stack.append(score_stack[-1]*2)
            elif e == 'C' and score_stack:
                score_stack.pop()
            elif e == '+' and len(score_stack)>=2:
                score_stack.append(score_stack[-1]+score_stack[-2])
            else:
                score_stack.append(int(e))
        return sum(score_stack)    

#Time complexity: O(n)
#Space complexity:O(n)           
