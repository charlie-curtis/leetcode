class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:


        out = []
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and spaces[j] == i:
                j+=1
                out.append(" ")
            out.append(s[i])

        return ''.join(out)
        