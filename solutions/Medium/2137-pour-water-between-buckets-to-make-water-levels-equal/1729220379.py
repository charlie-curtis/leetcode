class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:

        l = 0
        r = 10**9
        total = sum(buckets)
        loss/=100

        def check(mid):
            cost = 0
            extra = sum([x-mid for x in buckets if x > mid])

            for x in buckets:
                if x < mid:
                    delta = abs(mid -x)
                    cost+= (delta/(1-loss))
            return cost <= extra


        #check(x) = true if you can fill each bucket with x water
        #TTTTTFFFFFFFFF
        mid = 0
        while r - l > 10**(-5):
            mid = l + (r-l)/2
            if check(mid):
                l = mid
            else:
                r = mid
        return mid 


