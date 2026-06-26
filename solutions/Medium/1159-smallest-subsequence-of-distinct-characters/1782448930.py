class Solution:
    def smallestSubsequence(self, s: str) -> str:

        last = {}
        for i,x in enumerate(s):
            last[x] = i
        
        out = []
        for i in range(len(s)):
            x = s[i]
            if x in out:
                continue
            while out and out[-1] > x and last[out[-1]] > i:
                out.pop()
            out.append(x)
        return ''.join(out)
        