class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        #7 +  3 + 4 + 3

        #i,j is the subarray of cuts
        #100*100*100 = 10^6, but each can take O(100) time, so 10^8?
        #i,j,k -> k is how many cuts you've already done
        cuts.sort()

        m = len(cuts)
        @cache
        def dp(i,j):
            if i > j:
                return 0

            lower = 0 if i == 0 else cuts[i-1]
            upper = n if j == m-1 else cuts[j+1]
            if upper - lower < 0:
                print(i,j, "BLA")
            ans = 1e15 
            for k in range(i,j+1):
                ans = min(ans, dp(i,k-1) + dp(k+1,j))


            ##need to handle boundaries
            return ans + upper-lower

        return dp(0, m-1)
        