from sortedcontainers import SortedDict
class MaxStack:

    def __init__(self):
        #we are using two different datastructures to solve this problem
        self.stack = SortedDict() #this will handle the pop/top ops
        self.maxHeap = SortedDict() #this will handle peekmax/popmax
        self.nxt_id = 1
        #they want this to be O(1)
        self.topItem = -1
        

    def push(self, x: int) -> None:
        id = self.nxt_id
        self.nxt_id+=1
        self.stack[id] = x
        self.topItem = x
        if x not in self.maxHeap:
            self.maxHeap[x] = deque()
        self.maxHeap[x].append(id)
        
    def pop(self) -> int:
        #get the maxId
        idx, x = self.stack.peekitem(-1)
        del self.stack[idx]

        #also need to update the maxHeap
        sanity = self.maxHeap[x].pop()
        if sanity != idx:
            raise ValueError("Wrong")
        
        if len(self.maxHeap[x]) == 0:
            del self.maxHeap[x]
        
        self.topItem = -1 if not self.stack else self.stack.peekitem(-1)[1]
        return x

    def top(self) -> int:
        return self.topItem
        

    def peekMax(self) -> int:
        return self.maxHeap.peekitem(-1)[0]

    def popMax(self) -> int:
        x, q = self.maxHeap.peekitem(-1)
        idx = q.pop()
        if len(q) == 0:
            del self.maxHeap[x]

        del self.stack[idx]
        self.topItem = -1 if not self.stack else self.stack.peekitem(-1)[1]

        return x
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()