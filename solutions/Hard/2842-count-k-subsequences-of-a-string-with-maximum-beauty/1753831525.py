class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:

        #editorial
        f = sorted(list(Counter(s).values()))

        if k > len(f):
            return 0

        cutoff = f[-k]
        ans = 1
        has = 0
        available = 0
        MOD = 10**9 + 7

        #CHOOSE SUBSEQUENCES FIRST
        for x in f:
            if x > cutoff: #this is definitely included
                has+=1
                ans*=x # x choose 1
                ans%=MOD
            elif x == cutoff:
                available+=1
            
        if has == k:
            return ans
        needed = k-has

        ans*=(comb(available, needed) % MOD)

        #FOR EACH SUBSEQUENCE, PICK THE CHARS INSIDE THEm

        ans *= pow(cutoff, needed, MOD)
        ans%=MOD
        return ans
        
