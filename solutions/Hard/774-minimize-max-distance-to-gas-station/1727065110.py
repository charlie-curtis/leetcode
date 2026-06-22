class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        l = 0
        r = 10**8+1

        def check(tolerance):
            n = len(stations)
            total = 0
            for i in range(1,n):
                dst = stations[i] - stations[i-1]
                total+=dst//tolerance
            return total<=k
                


        #FFFFFFFFFFTTTTTTT
        while r - l > 1e-6:
            mid = l + (r-l)/2
            if check(mid):
                r = mid
            else:
                l = mid
        return mid