class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:

        sweep = [0]*n

        for pos, radius in lights:
            start = max(pos-radius, 0)
            stop = pos+radius+1
            if stop < n:
                sweep[stop]-=1
            sweep[start]+=1

        
        cur = 0
        ans = 0
        for i in range(n):
            cur+=sweep[i]
            if cur >= requirement[i]:
                ans+=1
        return ans



        