class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:

        #Let's just cache the states and see if it ACs

        d = defaultdict(list)
        for a,b,w in highways:
            d[a].append([b,w])
            d[b].append([a,w])

        NEGINF = -(10**6)

        @cache
        def dp(state, cur):

            if state.bit_count() == k:
                return 0

            best = NEGINF
            state|=(1<<cur)
            for u,w in d[cur]:
                    seen = state&(1<<u) > 0
                    if not seen:
                        a = dp(state, u) + w
                        best = max(best, a)

            return best


        #print([dp(0,i,-1, 0) for i in range(n)])
        res = max([dp(0, i) for i in range(n)])

        return -1 if res < 0  else res


            
