
MOD = 10**9 + 7
@cache
def dp(cur, i):

    if cur == 0: return 1
    if cur < 0: return 0

    a = [1,2,6]
    if i == len(a):
        return 0

    ans = dp(cur, i+1) % MOD
    ans+= dp(cur-a[i], i) % MOD
    ans%=MOD
    return ans


class Solution:
    def numberOfWays(self, n: int) -> int:

        a = dp(n, 0)
        b = dp(n-4, 0)
        c = dp(n-8, 0)
    
        return (a + b + c) % MOD
        
        
        

        