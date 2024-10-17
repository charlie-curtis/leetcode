class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        n = len(s)
        C = Counter()

        j = 0
        ans = 0
        for i in range(n):
            C[s[i]]+=1

            if i-j+1 > k:
                C[s[j]]-=1
                if C[s[j]] == 0:
                    del C[s[j]]
                j+=1
            if i-j+1 == k:
                ans+=1 if len(C.keys()) == k else 0
        return ans

        