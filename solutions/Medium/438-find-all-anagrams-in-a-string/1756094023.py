class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        C = Counter(p)
        m,n = len(s), len(p)

        j = 0
        C1 = Counter()
        out = []
        for i in range(m):
            C1[s[i]]+=1
            if i-j+1 > n:
                C1[s[j]]-=1
                if C1[s[j]] == 0:
                    del C1[s[j]]
                j+=1
            if C1 == C:
                out.append(j)
        return out

        