class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:


        seen = set()
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                g = gcd(i,j)
                a = str(i//g)
                b = str(j//g)
                seen.add(a + "/" + b)
        return list(seen)