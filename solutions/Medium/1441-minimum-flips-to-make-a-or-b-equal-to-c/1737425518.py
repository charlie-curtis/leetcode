class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        ans = 0
        for i in range(40):
            ai = int(a&(1<<i) > 0)
            bi = int(b&(1<<i) > 0)
            ci = int(c&(1<<i) > 0)

            if ci:
                if ai + bi == 0: ans+=1
            else:
                ans+=ai
                ans+=bi
        return ans
            
        