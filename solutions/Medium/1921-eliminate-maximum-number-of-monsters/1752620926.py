class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        #sort by when they reach the city
        A = sorted([d/s for (d,s) in zip(dist, speed)])

        ans = 1
        for i,x in enumerate(A[1:]):
            if x <= i+1:
                return ans
            ans+=1
        return ans
        

        