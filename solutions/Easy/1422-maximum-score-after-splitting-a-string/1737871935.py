class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = 0
        ans = 0
        for i,x in enumerate(s[:-1]):
            if x == '0':
                zeros+=1
            else:
                ones-=1
            ans = max(ans, zeros+ones)
        return ans