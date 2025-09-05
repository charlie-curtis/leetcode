class Node:
    def __init__(self, val):
        self.fwd = None
        self.back = None
        self.val = val
class RandomizedSet:

    def __init__(self):
        self.A = ['']*(10**5+1)
        self.H = {}
        self.n = 0
        

    def insert(self, val: int) -> bool:
        if val in self.H:
            return False
        self.H[val] = self.n
        self.A[self.n] = val
        self.n+=1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.H:
            return False
        pos = self.H[val]
        del self.H[val]
        if pos != self.n-1:
            #swap to end
            last_val = self.A[self.n-1]
            self.H[last_val] = pos
            self.A[pos] = last_val
        self.n-=1
        return True

    def getRandom(self) -> int:
        x = randint(0, self.n-1)
        x = randint(0, self.n-1)
        return self.A[x]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()