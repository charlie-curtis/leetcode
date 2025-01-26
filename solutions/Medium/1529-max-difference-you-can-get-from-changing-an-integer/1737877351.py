class Solution:
    def maxDiff(self, num: int) -> int:

        low = num
        high = num
        ans = 0
        s = str(num)
        n = len(s)
        for i in range(10):
            for j in range(10):
                a = s.replace(str(i), str(j))
                if a[0] == '0':
                    continue
                high = max(high, int(a))
                low = min(low, int(a))

        return high-low
                
                