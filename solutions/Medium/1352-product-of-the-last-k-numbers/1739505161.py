class ProductOfNumbers:

    def __init__(self):
        self.p=[]
        

    def add(self, num: int) -> None:
        if num==0: self.p=[]
        elif not self.p: self.p=[num]
        else: self.p.append(self.p[-1]*num)

        
        

    def getProduct(self, k: int) -> int:
        if len(self.p) < k:return 0
        if len(self.p) == k: return self.p[-1]
        a=self.p[-1]
        b=self.p[-1-k]
        return a // b
        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)