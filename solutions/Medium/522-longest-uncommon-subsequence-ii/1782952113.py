class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda x: -len(x))
        
        def issub(s1,s2):
            i = 0
            n = len(s2)
            for x in s1:
                if i==n:
                    break
                if x == s2[i]:
                    i+=1
            return i == n
            
        n=len(strs)
        for i in range(n):
            good=True
            for j in range(n):
                if i == j:
                    continue
                if issub(strs[j], strs[i]):
                    good=False
                    break
            if good:
                return len(strs[i])
        return -1