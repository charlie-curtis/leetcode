class Solution:
    def makesquare(self, A: List[int]) -> bool:


        ssum = sum(A)
        if ssum % 4:
            return False
        target = ssum // 4

        n = len(A)
        @cache
        def dp(used,rem, cnt):
            if rem < 0:
                return False
            if cnt == 4 and used == 2**n - 1 and rem == target:
                return True
            if rem == 0:
                return dp(used, target, cnt+1)
            

            for i in range(n):
                if used&(1<<i) == 0:
                    if dp(used|(1<<i), rem-A[i], cnt):
                        return True
            return False
        
        return dp(0,target, 0)


        