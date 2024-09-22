class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        j = ans = 0
        n = len(s)
        c = Counter()
        for i in range(n):
            c[s[i]]+=1
            while len(c.keys()) > 2:
                c[s[j]]-=1
                if c[s[j]] == 0:
                    del c[s[j]]
                j+=1
            
            ans = max(ans, i-j+1)
        return ans
            
        