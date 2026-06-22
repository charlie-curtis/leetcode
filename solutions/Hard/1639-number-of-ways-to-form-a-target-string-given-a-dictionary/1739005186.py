class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        m = len(words)
        n = len(words[0])
        p = len(target)
        M = 10**9 + 7


        C = Counter()
        for word in words:
            for k,x in enumerate(word):
                C[(k,x)]+=1
        @cache
        def dp(i,k):
            if i == p:
                return 1
            if k >= n:
                return 0


            #try to satisfy the i-th character from target using the k-th character from any of the words
            x = target[i]
            v = C[(k,x)]
            ans = v*dp(i+1, k+1)
            ans%=M

            #don't use this
            ans+=dp(i, k+1)
            ans%=M
            return ans
        return dp(0,0)
            
            

        