cutoff = (10**5)
P = [True]*(cutoff+1)
P[0] = P[1] = False
i = 2
for i in range(2, int(sqrt(cutoff)) +1):
    if P[i]:
        for j in range(2, int(cutoff//i)+1):
            P[i*j] = False

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        return abs(sum([x if P[i] else -x for i,x in enumerate(nums)]))