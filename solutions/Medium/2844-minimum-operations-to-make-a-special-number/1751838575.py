class Solution:
    def minimumOperations(self, num: str) -> int:

        #need to make the last two numbers end in '00', '25', '50', or '75'

        n = len(num)
        ans = n if '0' not in num else n-1
        for digit in ['00', '25', '50', '75']:
            L = digit[0]
            R = digit[1]
            i = num.rfind(R)
            if i == -1:
                ans = min(ans, n)
                continue
            i = num.rfind(L, 0, i)
            if i == -1:
                ans = min(ans, n)
                continue
            
            ans = min(ans, n-i-2)
        return ans
            
        