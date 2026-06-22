class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:


        n = len(jobs)
        @cache
        def dp(i, rem):
            if i == n:
                if rem != 0:
                    return 1e15
                return 0
            if rem == 0:
                return 1e15


            mmax = 0
            ans = 1e15 
            for j in range(i,n):
                mmax = max(mmax, jobs[j])
                ans = min(ans, dp(j+1, rem-1) + mmax)
            return ans
        res = dp(0, d)
        if res>= 1e15:
            return -1
        return res
                
        