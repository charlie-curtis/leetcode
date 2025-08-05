class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        m,n = len(g), len(s)
        j = ans = 0
        for i in range(m):
            while j < n and g[i] > s[j]:
                j+=1
            if j < n:
                ans+=1
                j+=1
            else:
                break
        return ans
        