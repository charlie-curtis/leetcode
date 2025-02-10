class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n=len(seats)
        
        locs=[i for i  in range(n) if seats[i]]
        
        ans=max(locs[0],n-1-locs[-1])
        for a,b in zip(locs, locs[1:]):
            ans=max(ans,(b-a)//2)
        return ans