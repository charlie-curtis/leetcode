class Solution:
    def countPairs(self, D: List[int]) -> int:


        C = Counter()
        MOD = 10**9 + 7
        mx = max(D)

        ans = 0
        for x in D:
            cur = 1
            while cur <= 2*mx:
                ans+= C[cur-x]
                ans%=MOD
                cur<<=1
            C[x]+=1
        return ans

        