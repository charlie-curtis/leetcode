class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:


        n = len(s)
        def score(streak):
            if streak in [-1, 0]:
                return 0
            return min(streak, len(str(streak))+1)
        @cache
        def dp(i, prev, k, streak):
            if k < 0:
                return 1e15
            if i == n:
                if prev == -1:
                    return 1e15
                return score(max(0,streak-k))
            
            #don't do anything -- keep it in answer
            #if our char changes, then we need to calc it
            a = b = 1e15
            if prev != s[i]:
                a = dp(i+1, s[i], k, 1)  + score(streak)
            else:
                a = dp(i+1, s[i], k, streak+1)

            #delete the char
            b = dp(i+1, prev, k-1, streak)

            return min(a,b)
        return dp(0, -1, k, -1)