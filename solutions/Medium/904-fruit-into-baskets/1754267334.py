class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        n = len(fruits)

        j = 0
        C = Counter()
        ans = 0
        for i,x in enumerate(fruits):
            C[x]+=1
            while len(C.keys()) > 2:
                C[fruits[j]]-=1
                if C[fruits[j]] == 0:
                    del C[fruits[j]]
                j+=1
            ans = max(ans, i-j+1)
        return ans
            