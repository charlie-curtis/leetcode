#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        c = Counter()
        j = 0
        ans = 0
        for i,x in enumerate(s):
            c[x]+=1
            while c[x] > 1:
                c[s[j]]-=1
                j+=1
            ans = max(ans, i-j+1)
        return ans
