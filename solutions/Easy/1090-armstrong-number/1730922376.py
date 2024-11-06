class Solution:
    def isArmstrong(self, n: int) -> bool:

        s = str(n)
        ans = 0
        for x in s:
            ans+=int(x)**(len(s))

        return ans == n

        