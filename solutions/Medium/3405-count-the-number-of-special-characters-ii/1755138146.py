class Solution:
    def numberOfSpecialChars(self, word: str) -> int:


        ans = 0
        for i in range(26):
            c = chr(i + ord('a'))
            C = c.upper()
            last = word.rfind(c)
            first = word.find(C)
            if last != -1 and first != -1 and last < first:
                ans+=1


        return ans
        