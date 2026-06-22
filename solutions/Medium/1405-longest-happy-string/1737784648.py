class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        pq = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        pq = [[v,k] for v,k in pq if v != 0]
        heapify(pq)
        ans = []
        ht = []
        while pq:
            v, c = heappop(pq)
            v = abs(v)
            if ht:
                heapq.heappush(pq, ht)
                ht = []
            if ans and len(ans) >= 2 and (ans[-1] == ans[-2] == c):
                ht = [-v, c]
            else:
                ans.append(c)
                if v-1 > 0:
                    heapq.heappush(pq, [-(v-1), c])
        return ''.join([x for x in ans])
        '''
        def dp(a,b,c, avoid):
            if min(a,b,c) == 0:
                return 0

            ans = 0
            if avoid != 'a':
                for i in range(min(3,a+1)):
                    ans = max(ans, i+1 + dp(a-i-1, b,c, 'a'))
            if avoid != 'b':
                for i in range(min(3,b+1)):
                    ans = max(ans, i+1 + dp(a, b-i-1,c, 'b'))
            if avoid != 'c':
                for i in range(min(3,c+1)):
                    ans = max(ans, i+1 + dp(a, b,c-i-1, 'c'))
            return ans

        return dp(a,b,c, '')
        '''
        
                
