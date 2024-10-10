class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        n = len(s)
        ans = 0
        C = Counter()
        j = 0

        for i in range(n):
            C[s[i]]+=1

            while len(C.keys()) > k:
                C[s[j]]-=1
                if C[s[j]] == 0:
                    del C[s[j]]
                j+=1
            ans = max(ans, i-j+1)
        return ans


        