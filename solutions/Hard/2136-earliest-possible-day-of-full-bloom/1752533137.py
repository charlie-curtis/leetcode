class Solution:
    def earliestFullBloom(self, plant: List[int], grow: List[int]) -> int:

        A = list(zip(plant, grow))
        A.sort(key= lambda x: -x[1])

        t = 0 # time
        ans = 0
        for p,g in A: #plant, grow. Sort by the bottleneck (e.g. longest growing)
            t+=p #increment our time by however long it takes to plant
            ans = max(ans, t+g) #the answer is max of previous answer OR whatever the current time is plus the time it takes to grow
        return ans
        