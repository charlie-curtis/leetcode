class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:


        def good(state):
            C = Counter()
            for i,(x,y) in enumerate(requests):
                if state&(1<<i) > 0:
                    C[x]-=1
                    C[y]+=1
            if len(C.keys()) == 0:
                return True
            return max(C.values()) == min(C.values()) == 0
        m = len(requests)
        @cache
        def dp(i, state):

            if i == m:
                if good(state):
                    return 0
                return -1e15 

            a = dp(i+1, state|(1<<i)) + 1
            b = dp(i+1, state)
            return max(a,b)

        return dp(0,0)
        