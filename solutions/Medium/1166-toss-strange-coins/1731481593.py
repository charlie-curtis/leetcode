class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:



        n = len(prob)
        @cache
        def dp(i, rem):

            if i == n:
                return int(rem == 0)
            if rem < 0:
                return 0

            
            p_head = dp(i+1, rem-1)*prob[i]
            p_tails = dp(i+1, rem)*(1-prob[i])
            return p_head+p_tails

        
        return dp(0, target)
        