class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        for x in s:
            found = False
            while i < len(t):
                if x == t[i]:
                    i+=1
                    found = True
                    break
                i+=1
            if not found:
                return False
        return True
                

        