class Solution:
    def maxRemovals(self, s: str, p: str, targetIndices: List[int]) -> int:

        targets = set(targetIndices)
        m,n = len(s), len(p)

        dp = [[float('-inf') for _ in range(n+1)] for _ in range(m+1)]
        k = len(targetIndices)
        t = 0
        for i in range(m+1):
            #t should rest on first idx gte i
            while t < k and targetIndices[t] < i:
                t+=1
            #if we reach our pattern, then it's valid for any char to the right
            dp[i][n] = k - t 

        #dp(i,j) = max score we can get from starting at i,j (suffix)
        for i in range(m-1, -1, -1):
            for j in range(n-1,-1,-1):
                special = i in targets
                matches = s[i] == p[j]

                #transitions
                #if it matches, we can use the char and go i+1, j+1
                #we can always not use the ith character, so i+1, j, and we add +1 if it's special

                #if we DON'T use this char, j stays the same and we can unlock

                if matches:
                    #we can either use it or not use it
                    dp[i][j] = max(dp[i+1][j+1], dp[i+1][j] + int(special))
                else:
                    #we don't use the char
                    dp[i][j] = dp[i+1][j] + int(special)
        return dp[0][0]