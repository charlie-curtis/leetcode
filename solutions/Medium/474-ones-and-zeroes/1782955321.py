class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        L = len(strs)
        cnts = [[0,0] for _ in range(L)]

        for i in range(L):
            zeros = strs[i].count('0')
            ones = strs[i].count('1')
            cnts[i][0] = zeros
            cnts[i][1] = ones

        #600*100*100 = 6*10^6

        @cache
        def dp(i,zeros, ones):
            if zeros > m or ones > n:
                return -10**9
            if i == L:
                return 0
            
            a = dp(i+1, zeros,ones)
            b = 1 + dp(i+1, zeros+cnts[i][0], ones + cnts[i][1])

            return max(a,b)

        
        return dp(0,0,0)

