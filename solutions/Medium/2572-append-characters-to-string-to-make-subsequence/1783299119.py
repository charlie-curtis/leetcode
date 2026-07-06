class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        m,n = len(s), len(t)

        i = 0
        for x in s:
            if x == t[i]:
                i+=1
            
            if i == n:
                break
        
        return n-i
        