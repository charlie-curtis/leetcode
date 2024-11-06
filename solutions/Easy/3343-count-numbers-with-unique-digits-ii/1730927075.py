class Solution:
    def numberCount(self, a: int, b: int) -> int:

        ans = 0
        for x in range(a, b+1):

            y = x
            seen = set()
            good = True
            while y > 0:
                digit = y % 10
                if digit in seen:
                    good = False
                    break
                seen.add(digit)
                y//=10
            if good:
                ans+=1
        return ans
        