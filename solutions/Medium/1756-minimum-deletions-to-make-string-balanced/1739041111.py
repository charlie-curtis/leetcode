class Solution:
    def minimumDeletions(self, s: str) -> int:

        aC = s.count('a')
        bC = 0
        ans = aC
        for i,x in enumerate(s):
            if x == 'b':
                bC+=1
            else:
                aC-=1
            ans = min(ans, bC + aC)
        return ans
        