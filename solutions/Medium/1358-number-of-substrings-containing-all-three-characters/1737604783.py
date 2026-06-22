class Solution:
    def numberOfSubstrings(self, s: str) -> int:


        n = len(s)
        j = 0
        ans = 0
        C = Counter()

        for i in range(n):
            C[s[i]]+=1

            while C['a'] > 0 and C['b'] > 0 and C['c'] > 0:
                C[s[j]]-=1
                j+=1
            ans+=j
        return ans