class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:

        #for each j, try to pair it with one or more quantities
        A = sorted(Counter(nums).values())[::-1]
        quantity.sort(reverse=True)
        n = len(quantity)
        @cache
        def dp(state, j, prev):
            if state == 2**n-1:
                return True
            if j == len(A):
                return False

            #we don't use this value
            if dp(state, j+1, -1):
                return True

            prev = A[j] if prev == -1 else prev
            for i in range(n):
                if (state >> i) & 1 == 0: #we haven't used this num
                    if prev >= quantity[i]:
                        if dp(state|(1<<i), j, prev-quantity[i]):
                            return True
                        if dp(state|(1<<i), j+1, -1):
                            return True
            return False

        return dp(0, 0, -1)
                        
                    
        