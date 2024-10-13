class Solution:
    def canWin(self, currentState: str) -> bool:



        @cache
        def canWinDp(state):

            n = len(state)
            for i in range(n-1):
                if '++' == state[i:i+2] and not canWinDp(state[:i] + '--' + state[i+2:]):
                    return True
            return False

        return canWinDp(currentState)

        
        