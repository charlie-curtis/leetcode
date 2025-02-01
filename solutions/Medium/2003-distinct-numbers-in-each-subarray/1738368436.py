class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:



        n = len(nums)
        out = []
        j = 0
        C = Counter()
        for i in range(n):
            C[nums[i]]+=1

            if i-j+1 > k:
                C[nums[j]]-=1
                if C[nums[j]] == 0:
                    del C[nums[j]]
                j+=1
            
            if i-j+1 == k:
                out.append(len(C.keys()))

        return out

        