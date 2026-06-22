class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        l = 0
        r = 2*10**15

        def check(mid):
            a = sum([floor(sqrt(mid/r)) for r in ranks])
            return a >= cars

        while l<=r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
        