class Bank:

    def __init__(self, balance: List[int]):
        self.b = balance

    def valid(self,n):
        return 1 <= n <= len(self.b)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.valid(account1) or not self.valid(account2):
            return False
        account1-=1
        account2-=1
        if self.b[account1]>=money:
            self.b[account1]-=money
            self.b[account2]+=money
            return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if not self.valid(account):
            return False
        account-=1

        self.b[account]+=money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if not self.valid(account):
            return False
        account-=1
        if self.b[account]>=money:
            self.b[account]-=money
            return True
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)