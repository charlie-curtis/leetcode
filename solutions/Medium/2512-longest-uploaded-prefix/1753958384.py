class LUPrefix:

    def __init__(self, n: int):
        self.L = set()
        self.cur = 0
        

    def upload(self, video: int) -> None:
        self.L.add(video)
        while self.cur+1 in self.L:
            self.cur+=1
        
        

    def longest(self) -> int:
        return self.cur
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()