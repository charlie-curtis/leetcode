class Solution:
    def isBalanced(self, num: str) -> bool:

        odd = even = 0
        s = str(num)
        for i in range(len(s)):
            if i % 2 == 0:
                even+=int(s[i])
            else:
                odd+=int(s[i])
        return odd == even
            
        