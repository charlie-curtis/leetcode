class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        j = 0
        C = Counter()
        ans = 0
        for i in range(len(s)):
            letter = s[i]
            C[letter]+=1
            while C[letter] > 1:
                C[s[j]]-=1
                j+=1
            ans = max(ans, i-j+1)
        return ans

        