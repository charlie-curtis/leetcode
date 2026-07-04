class Solution:
    def powerUpdate(self, nums: list[int], p: int, queries: list[list[int]]) -> list[int]:


        sl = SortedList(nums)
        MOD = 10**9 + 7

        @cache
        def fexp(p, x):
            if x == 0:
                return 1
            
            if x % 2 == 0:
                a = 1
                a*=fexp(p, x//2)
                a%=MOD
                a*=fexp(p, x//2)
                a%=MOD
            else:
                a = p
                a*=fexp(p, x-1)
                a%=MOD
            return (a % MOD)

        out = []
        for val, k in queries:
            sl.add(val)
            x = sl[-k]
            p = fexp(p, x)
            out.append(p)
        return out
        