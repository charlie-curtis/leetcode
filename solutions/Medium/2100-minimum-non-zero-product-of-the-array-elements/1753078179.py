class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD=10**9 + 7


        base=pow(2,p,MOD)
        a = (base - 1 + MOD) % MOD
        b = (base-2 + MOD) % MOD
        c=pow(b,(2**p-2)//2,MOD)

        ans=a
        ans%=MOD
        ans*=c
        ans%=MOD
    
        return ans