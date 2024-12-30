class Solution:
    def minOperations(self, initial: str, target: str) -> int:

        '''
        m,n = len(initial), len(target)
        def check(k):
            sset = set()
            for i in range(n-k+1):
                sset.add(target[i:i+k])
            
            j = 0
            for i in range(m-k+1):
                if initial[i:i+k] in sset:
                    return True
            return False


        #TTTFFFF

        l = 0
        r = min(m,n)

        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid -1


        return (m-r) + (n-r)

        '''

        m,n = len(initial), len(target)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        best = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                a = initial[i-1]
                b = target[j-1]
                if a == b:
                    dp[i][j] = 1 + dp[i-1][j-1]

                best = max(best, dp[i][j])

        return m - best + n - best