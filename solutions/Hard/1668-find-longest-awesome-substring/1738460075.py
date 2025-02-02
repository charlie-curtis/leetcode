class Solution:
    def longestAwesome(self, s: str) -> int:


        #palindrome - every number (except for possibly one) shows up an even number of times

        def check(state, d):
            can = 0
            if state in d:
                can = i - d[state]

            tmp = state
            for j in range(10):
                tmp = state^(1<<j)
                if tmp in d:
                    can = max(can, i - d[tmp])
            return can

        n = len(s)
        d = {}
        d[0] = -1
        ans = 0
        state = 0
        for i in range(n):

            v = int(s[i])
            state^=(1<<v)

            can = check(state, d)
            
            ans = max(can, ans)
            if state not in d:
                d[state] = i
        return ans
            
            
        