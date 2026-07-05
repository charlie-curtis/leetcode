class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        C = Counter(nums)
        C2 = Counter()

        for k,v in C.items():
            C2[v]+=1
        
        for x in nums:
            f = C[x]
            if C2[f] == 1:
                return x
        return -1
        