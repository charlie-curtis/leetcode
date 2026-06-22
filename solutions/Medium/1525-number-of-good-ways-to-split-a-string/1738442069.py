class Solution:
    def numSplits(self, s: str) -> int:
        C1 = Counter()
        C2 = Counter(s)
        n = len(s)
        ans = 0
        for i in range(n-1):
            C1[s[i]]+=1
            C2[s[i]]-=1
            if C2[s[i]] == 0:
                del C2[s[i]]
            if len(C1.keys()) == len(C2.keys()):
                ans+=1
        return ans
            
        