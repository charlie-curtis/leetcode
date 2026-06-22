class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:


        C = Counter()
        for i in range(55):
            for x in nums:
                C[i]+=1 if x&(1<<i) > 0 else 0


        ans = 0
        for i in range(55):
            if C[i] > 0:
                ans|=(1<<i)
                C[i+1]+= C[i]//2
        return ans