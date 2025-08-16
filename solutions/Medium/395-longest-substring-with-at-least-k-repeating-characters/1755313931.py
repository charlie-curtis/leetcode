class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        #editorial, O(26N) - I should have gotten this one
        L = len(set(s))

        ans = 0
        for l in range(1, L+1):
            j = completed = 0
            C = Counter()
            for i,x in enumerate(s):
                C[x]+=1
                if C[x] == k:
                    completed+=1
                while len(C.keys()) > l:
                    if C[s[j]] == k:
                        completed-=1
                    C[s[j]]-=1
                    if C[s[j]] == 0:
                        del C[s[j]]
                    j+=1
                if completed == l:
                    ans = max(ans, i-j+1)
        return ans

