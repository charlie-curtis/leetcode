class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.d = defaultdict(int)
        for i,x in enumerate(products):
            self.d[x] = prices[i]
        self.count = 0
        self.n = n
        self.discount = discount
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        cost = 0
        self.count+=1
        for i,id in enumerate(product):
            cost+=self.d[id]*amount[i]

        if self.count % self.n == 0:
            cost = cost * ((100-self.discount) / 100)
        return cost
        
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)