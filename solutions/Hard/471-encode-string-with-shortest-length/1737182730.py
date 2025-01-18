class Solution:
    def encode(self, s: str) -> str:

        def getlength(cnt, t):
            used = str(cnt)
            return 2 + len(used) + len(t)

        def isgood(i,j,k):

            seen = set()
            if (j-i+1) %k != 0:
                return False
            for l in range(i, j+1, k):
                seen.add(s[l:l+k])
                if len(seen) > 1:
                    return False
            return True

        def to_string(cnt, s):
            if cnt == 1:
                return s
            return str(cnt) + "[" + s + "]"




        @cache
        def dp(i,j):
            if i == j:
                return [1, 1, s[i]]
            if i > j:
                raise ValueError("Wrong", i,j)


            best = [j-i+1, 1, s[i:j+1]]
            for k in range(i,j):
                l1, c1, t1 = dp(i, k)
                l2, c2, t2 = dp(k+1, j)

                if t1 == t2:
                    l1 = getlength(c1+c2, t1)
                    if l1 < best[0]:
                        best = [l1, c1+c2, t1]
                else:
                    if l1+l2 < best[0]:
                        best = [l1+l2, 1, to_string(c1,t1)+to_string(c2,t2)]
            
            for L in range(1, j-i+1+1):
                if isgood(i,j,L):
                    used = (j-i+1)//L
                    l1 = getlength(used, s[i:i+L])
                    if l1 < best[0]:
                        best = [l1, used, s[i:i+L]]
            return best


            
            return best

        res = dp(0, len(s)-1)
        cnt = res[1]
        t = res[2]

        return to_string(cnt, t)
