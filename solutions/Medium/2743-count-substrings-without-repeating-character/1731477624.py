class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:



        j = 0
        n = len(s)
        ans = 0
        C = Counter()
        for i in range(n):
            C[s[i]]+=1


            while C[s[i]] > 1:
                C[s[j]]-=1
                j+=1
            ans+=i-j+1

        return ans

        