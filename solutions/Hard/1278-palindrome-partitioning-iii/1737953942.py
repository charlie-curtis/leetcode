class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        n = len(s)
        costs = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                cost = 0
                l = i
                r = j
                while l < r:
                    if s[l] != s[r]:
                        cost+=1
                    l+=1
                    r-=1
                costs[i][j] = cost

        k-=1 #don't focus on the groups, focus on the number of times we split
        @cache
        def dp(i,split):
            if split > k:
                return 1e15
            if i >= n:
                split-=1
                #this isn't a valid split, so don't count it
                return 0 if split == k else 1e15
            
            ans = costs[i][n-1] if split == k else 1e15
            for l in range(i,n):
                ans = min(ans, costs[i][l] + dp(l+1, split+1))
            return ans

        return dp(0, 0)


        