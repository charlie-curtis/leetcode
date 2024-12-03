class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.diag = 0
        self.rows = Counter()
        self.cols = Counter()
        self.antidiag = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        i,j = row, col

        v = 1 if player==1 else -1
        self.rows[i]+=v
        self.cols[j]+=v
        if i == j:
            self.diag+=v
        if i == n-1-j:
            self.antidiag+=v

        if self.rows[i] == n or self.cols[j] == n or self.diag == n or self.antidiag == n:
            return 1
        if self.rows[i] == -n or self.cols[j] == -n or self.diag == -n or self.antidiag == -n:
            return 2

        return 0
        



        # 0 0 0
        # 0 0 0
        # 0 0 0

        #i = j
        #n-1-i, n-1-j
        #2,0
        #1,1
        #0,2
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)