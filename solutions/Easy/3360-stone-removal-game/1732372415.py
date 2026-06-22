class Solution:
    def canAliceWin(self, n: int) -> bool:

        isAlice=True
        stones = 10
        while True:
            if stones == 0 or n < stones:
                return not isAlice

            n-=stones
            stones-=1
            isAlice = not isAlice
            
        