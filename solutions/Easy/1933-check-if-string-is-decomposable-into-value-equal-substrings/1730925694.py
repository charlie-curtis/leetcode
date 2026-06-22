class Solution:
    def isDecomposable(self, s: str) -> bool:


        lifelines = 0

        for char, group in groupby(s):
            n = len(list(group))

            #cases
            #1. the number is div by 3
            if n % 3 == 0:
                continue
            #2. the number is div by 3 after subtracting 2, but we can only do this once
            if n>=2 and (n-2) % 3 == 0:
                lifelines+=1
                continue
            
            #everything else fails
            return False


        return lifelines == 1
