class Leaderboard:

    def __init__(self):
        self.d = {}

    def addScore(self, playerId: int, score: int) -> None:

        cur = 0
        if playerId in self.d:
            cur = self.d[playerId]
        self.d[playerId] = cur + score
        

    def top(self, K: int) -> int:
        A = sorted(self.d.values(), reverse=True)
        ans = 0
        for i in range(min(len(A), K)):
            ans+=A[i]
        return ans

        

    def reset(self, playerId: int) -> None:
        self.d[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)