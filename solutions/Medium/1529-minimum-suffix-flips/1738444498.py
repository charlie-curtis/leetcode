class Solution:
    def minFlips(self, target: str) -> int:



        #00000
        #0000111
        #0011000
        #0010111
        #1101000
        #1010111

        ans = 0
        seen = False
        for c, g in groupby(target[::-1]):
            if c == '0':
                seen = True
                continue
            ans+=1 if not seen else 2
        return ans