class Solution:
    def nimGame(self, piles: List[int]) -> bool:

        @cache
        def bt(state):

            state = list(state)
            for i,x in enumerate(state):
                if x == 0:
                    continue #not eligible
                for j in range(1,x+1):
                    state[i]-=j
                    if not bt(tuple(state)):
                        return True
                    state[i]+=j
            return False
        
        return bt(tuple(piles))

        