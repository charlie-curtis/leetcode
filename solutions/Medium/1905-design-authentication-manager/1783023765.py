class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.d = defaultdict(int)
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.d[tokenId] = currentTime + self.ttl

        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.d[tokenId] and self.d[tokenId] > currentTime:
            self.generate(tokenId, currentTime)
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        reaper = []
        for k,v in self.d.items():
            if v <= currentTime:
                reaper.append(k)
            else:
                cnt+=1
        for k in reaper:
            del self.d[k]
        return cnt


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)