class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        def check(S, T):
            n = len(S)
            i,j = 0, n-1

            sUsable = True
            tUsable = True
            while i < j:
                if sUsable and S[i] != T[j]:
                    sUsable = False
                if not sUsable and tUsable and T[i] != T[j]:
                    tUsable = False

                if not sUsable and not tUsable:
                    #print("max I found was", 2*i, "and the length of the string was", n)
                    return False
                i+=1
                j-=1
            return True


        return check(a,b) or check(b,a) or check(a[::-1], b[::-1]) or check(b[::-1], a[::-1])