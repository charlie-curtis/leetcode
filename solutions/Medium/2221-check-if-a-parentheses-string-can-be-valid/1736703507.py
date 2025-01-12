class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        #editorial
        open = []
        free = []
        for i,x in enumerate(s):
            
            L = locked[i] == '1'
            if not L:
                free.append(i)
            elif x == '(':
                open.append(i)
            else:
                if open:
                    open.pop()
                elif free:
                    free.pop()
                else:
                    return False

        while free and open and open[-1] < free[-1]:
            free.pop()
            open.pop()
        if open:
            return False
        if len(free) % 2 == 1:
            return False
        return True