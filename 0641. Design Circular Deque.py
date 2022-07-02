641. Design Circular Deque
https://leetcode.com/problems/design-circular-deque/
  
class MyCircularDeque:

    def __init__(self, k: int):
        self.queue=deque([])
        self.size=k

    def insertFront(self, value: int) -> bool:
        
        if len(self.queue)<self.size:
            self.queue.insert(0,value)
            return True
        return False
    
    def insertLast(self, value: int) -> bool:
        if len(self.queue) <self.size:
            self.queue.append(value)
            return True
        return False
    
    def deleteFront(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if self.queue:
            self.queue.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0
            
    def isFull(self) -> bool:
        return len(self.queue) == self.size
      
      
