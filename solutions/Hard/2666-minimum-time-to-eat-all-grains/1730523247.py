class Solution:
    def minimumTime(self, pos: List[int], grains: List[int]) -> int:

        pos.sort()
        grains.sort()
        m,n = len(pos), len(grains)

        def check(mid):
            j = 0
            for i in range(m):
                low = high = pos[i]
                while j < n:
                    low = min(low, grains[j])
                    high = max(high, grains[j])
                    d1 = abs(low - pos[i]) + 2*abs(pos[i] - high)
                    d2 = 2*abs(low - pos[i]) + abs(pos[i] - high)
                    if min(d1, d2) <= mid:
                        j+=1
                    else:
                        break
                if j == n:
                    return True


            return False

        l, r = 0, 10**15
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1
        return l
        