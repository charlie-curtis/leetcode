class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        m,n,l = len(s1), len(s2), len(s3)

        if m + n != l:
            return False

        @cache
        def dp(i,j, usei):
            if i + j == m + n:
                return True
            if usei and i == m:
                return False
            if not usei and j == n:
                return False

            if usei:
                for t in range(i,m):
                    k = t + j
                    if s1[t] == s3[k]:
                        if dp(t+1,j, False):
                            return True
                    else:
                        break
            else:
                for t in range(j,n):
                    k = t + i
                    if s2[t] == s3[k]:
                        if dp(i,t+1, True):
                            return True
                    else:
                        break

            
            return False
        
        return dp(0,0,False) or dp(0,0,True)

        