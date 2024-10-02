class Solution:
    def minLargest(self, A: List[int], B: List[int]) -> int:


        ans = 1e10
        @cache
        def dp(i,j, needs_odd):
            if i+j == len(A) + len(B):
                return 0
            
            options = []
            if i < len(A):
                cost = 1 if (needs_odd and (A[i] % 2 == 0)) or (not needs_odd and (A[i] % 2 == 1)) else 0
                tmp = not needs_odd if cost == 0 else needs_odd
                options.append(dp(i+1,j, tmp) + cost)
            if j < len(B):
                cost = 1 if (needs_odd and (B[j] % 2 == 0)) or (not needs_odd and (B[j] % 2 == 1)) else 0
                tmp = not needs_odd if cost == 0 else needs_odd
                options.append(dp(i,j+1, tmp) + cost)

            return min(options)

        c = dp(0,0, True)

        return len(A) + len(B) + c
