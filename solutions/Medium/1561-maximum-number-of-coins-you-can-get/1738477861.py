class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort(reverse=True)
        d = deque(piles)

        ans = 0
        while d:
            d.popleft()
            d.pop()
            ans+=d.popleft()
        return ans
            
        