class Solution:
    def numOfSubsequences(self, s: str) -> int:

        n = len(s)

        A = [1 if x == 'L' else 0 for x in s]
        preL = list(accumulate(A, initial = 0))
        A = [1 if x == 'T' else 0 for x in s]
        preT = list(accumulate(A, initial = 0))

        ans = 0
        #say we insert a 'C' at any given index
        boost = 0
        for i in range(0,n-1):
            #insert after i
            if s[i] == 'C':
                before = preL[i]
                after = preT[-1] - preT[i+1]
                ans+=(before*after)

            #assume we insert after i, so we can use i on the left side,but still not on the right
            before = preL[i+1]
            after = preT[-1] - preT[i+1]
            boost = max(boost, after*before)

        #now we have to see if we can beat the boost inserting L, T
        cnt = 0
        dp = [0]*n
        for i in range(n):
            if s[i] == 'L':
                cnt+=1
            if s[i] == 'C':
                dp[i]+=cnt
            if i > 0:
                dp[i]+= dp[i-1]
        #LLLCLLCTT

        cnt = 0
        dp2 = [0]*n
        for i in range(n-1, -1, -1):
            if s[i] == 'T':
                cnt+=1
            if s[i] == 'C':
                dp2[i]+=cnt
            if i < n-1:
                dp2[i]+= dp2[i+1]

        return ans + max(boost,dp[n-1], dp2[0] )
        
            
            