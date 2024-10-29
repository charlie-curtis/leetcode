class Solution:
    def minimumCoins(self, prices: List[int]) -> int:

        n = len(prices)
        pq = []
        if n == 1:
            return prices[0]
        
        #[cost to get here, last_usable_idx]
        q = deque()
        q.append([prices[0], 2])
        for i in range(1,n):

            while q[0][1] < i:
                q.popleft()
            
            my_best = q[0][0] + prices[i]
            while q and q[-1][0] >= my_best:
                q.pop()
            q.append([my_best, i+i+2])

        return q[0][0] if q[0][1] >= n else q[1][0]