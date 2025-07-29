class MKAverage:

    def __init__(self, m: int, k: int):
        self.q = deque()
        self.n = m
        self.k = k
        self.right = SortedList()
        self.left = SortedList()
        self.middle = SortedList()
        self.ssum = 0
        

    def addElement(self, num: int) -> None:
        q, n, k = self.q, self.n, self.k
        q.append(num)

        #print("adding num")

        if len(q) == n:
            #one time initialization
            #print("INIT")
            A = sorted(q)
            self.left = SortedList(A[:k])
            self.right = SortedList(A[-k:])
            self.middle = SortedList(A[k:-k])
            self.ssum = sum(self.middle)
        elif len(q) > n:
            v = q.popleft()
            if v in self.middle:
                self.middle.remove(v)
                self.ssum-=v
            elif v in self.left:
                self.left.remove(v)
            else:
                self.right.remove(v)
            
            if len(self.left):
                v = self.left.pop()
                self.middle.add(v)
                self.ssum+=v
            if len(self.right):
                v = self.right.pop(0)
                self.middle.add(v)
                self.ssum+=v
            self.middle.add(num)
            self.ssum+=num
            while len(self.left) < k:
                v = self.middle.pop(0)
                self.left.add(v)
                self.ssum-=v
            while len(self.right) < k:
                v = self.middle.pop(-1)
                self.right.add(v)
                self.ssum-=v
            
        #print(self.left, self.middle, self.right)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.n:
            return -1

        return self.ssum // (self.n - 2*self.k)
        
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()