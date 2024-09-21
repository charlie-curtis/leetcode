class Solution:
    def convertToTitle(self, t: int) -> str:


        ans = ""
        while t:
            t-=1
            v = t % 26
            t//=26
            ans = chr(ord('A')+v) + ans
        return ans
        
        