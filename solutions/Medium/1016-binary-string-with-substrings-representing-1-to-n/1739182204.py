class Solution:
    def queryString(self, s: str, n: int) -> bool:
        
        if n > 10**5: return False
        return all([bin(x)[2:] in s  for x in range(1,n+1)])
        