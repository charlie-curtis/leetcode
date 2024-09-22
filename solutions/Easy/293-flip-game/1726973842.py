class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:

        n = len(s)
        ans = []
        for i in range(n-1):
            if s[i:i+2] == '++':
                ans.append(s[:i] + '--' + s[i+2:])
        return ans
        