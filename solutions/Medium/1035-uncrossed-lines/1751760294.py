class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        H = defaultdict(list)
        for i,x in enumerate(nums2):
            H[x].append(i)
        

        m,n = len(nums1), len(nums2)
        '''
        @cache
        def dp(i,j):
            if i == m or j == n:
                return 0
            
            a = dp(i+1, j)
            can_idx = bisect_left(H[nums1[i]], j)
            if can_idx == len(H[nums1[i]]):
                return a
            nj = H[nums1[i]][can_idx]
            
            b = 1 + dp(i+1, nj+1)

            return max(a,b)

        return dp(0,0)
        '''

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        #dp[i,j] = max number of points that can be connected at a prefix (i,j)

        ans = 0
        for i in range(m):
            for j in range(n):
                #want to match the I
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = 1+dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[m][n]

        


        