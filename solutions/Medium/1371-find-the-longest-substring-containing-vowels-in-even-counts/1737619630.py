class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        #this stumped me on a virtual and i had to look at the editorial
        #I was playing around with binary search, prefix stuff, and sliding window


        mmap = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }

        d = {}
        d[0] = -1 


        C = Counter()
        n = len(s)
        ans = 0
        def get():
            out = 0
            for k,v in mmap.items():
                out+=(C[k]<<v)
            return out

        for i in range(n):
            if s[i] in mmap:
                C[s[i]]+=1
                C[s[i]]%=2


            state = get()
            if state in d:
                ans = max(ans, i-d[state])
            else:
                d[state] = i
        return ans