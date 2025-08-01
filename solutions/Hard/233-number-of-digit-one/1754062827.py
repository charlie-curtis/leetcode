class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        n = len(s)
        @cache
        def dp(i, tight):
            if i == n:
                return [1,0]

            cutoff = int(s[i]) if tight else 9
            paths = ones = 0
            for x in range(cutoff+1):
                #there are this many ways 
                prev_paths, prev_ones = dp(i+1, tight&(int(s[i]) == x))
                paths+=prev_paths
                ones+=prev_ones
                if x == 1:
                    ones+=prev_paths
            return [paths, ones]

        return dp(0, True)[1]
        