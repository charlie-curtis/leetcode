class Solution:
    def appealSum(self, s: str) -> int:

        #let's goooo. The idea is to do O(26*N). For each index, figure out when
        # the non-distinct characters enter a string. For example, "abbca" -> if we're processing idx = 0, the indices are [0,1,3,5] (we append n at the end). And the lengths are 1,2,2 respectively.
        #1*1 + 2*2 + 3*2 = 11 is the contribution for idx = 1. Repeat for the other indices
        n = len(s)
        nxt = [[n for _ in range(26)] for _ in range(n)]
        H = {}
        for i in range(n-1, -1, -1):
            H[s[i]] = i
            for j in range(0,26):
                c = chr(ord('a') + j)
                nxt[i][j] = H[c] if c in H else n

        ans = 0
        for i in range(n):
            st = set(nxt[i])
            st.add(n)
            V = sorted(st)

            for j in range(len(V)-1):
                s = V[j]
                e = V[j+1]
                ans+=(j+1)*(e-s)
        return ans
        