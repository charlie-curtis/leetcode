class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque(nums)
        self.C = Counter(nums)
        

    def showFirstUnique(self) -> int:
        while self.q and self.C[self.q[0]] > 1:
            self.q.popleft()
        
        return self.q[0] if self.q else -1
        

    def add(self, value: int) -> None:
        self.C[value]+=1
        self.q.append(value)
        
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)