class Solution:
    def doesAliceWin(self, s: str) -> bool:

        V = sum([1 if x in 'aeiou' else 0 for x in s])
        print(V)
        return V != 0
        