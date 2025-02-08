class Solution:
    def decrypt(self, nums: List[int], k: int) -> List[int]:



        n = len(nums)

        if k == 0:
            return [0]*n
        use_j = k > 0
        k = abs(k)

        j = 0
        out = [0]*n
        ssum = 0
        for i in range(n*2):
            ssum+=nums[i%n]
            if i-j+1 > k:
                ssum-=nums[j%n]
                j+=1

            if i-j+1 == k:
                if use_j:
                    out[(j-1)%n] = ssum
                else:
                    out[(i+1)%n] = ssum

        return out

