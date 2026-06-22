class Solution:
    def numberOfSteps(self, num: int) -> int:

        ans = 0
        x = num
        while x > 0:
            if x % 2 == 1:
                x-=1
            else:
                x//=2
            ans+=1
        return ans
        