class Solution:
    def maximizeWin(self, pos: List[int], k: int) -> int:

        n = len(pos)
        @cache
        def dp(i, rem):
            if i == n or rem == 0:
                return 0

            #simulate not using a segment - note i'm binary searching for an endpoint to jump
            #past duplicates. incrementing by i+1 also works
            nxt = bisect_left(pos,pos[i]+1)
            a = dp(nxt, rem)

            #simulate using a segment
            nxt = bisect_right(pos, pos[i]+k)
            v = nxt - i
            b = dp(nxt,rem-1) + v
            return max(a,b)
        
        return dp(0, 2)
        