class Solution:
    def compressedString(self, word: str) -> str:


        groups = groupby(word)

        ans = ""
        for c, g in groups:
            ll = len(list(g))
            whole = ll//9
            part = ll % 9
            ans+= (str(9)+c)*whole
            if part:
                ans+=str(part)+c
        return ans
