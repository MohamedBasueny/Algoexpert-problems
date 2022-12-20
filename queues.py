from collections import deque
#implementing Queue fifo 
class Queue:
    def __init__(self,*elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0 :
            yield  self.dequeue()

    def enqueue(self,element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

class stack(Queue) : 
    def dequeue(self): 
        return self._elements.pop()
    