class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        C = Counter()


        ans = 0
                #nums[i] - rev(nums[j]) = nums[j] - rev(nums[i])
        #If i store nums[i] - rev(nums[i]), then intuitively we're storing
        # how much of an imbalance we're creating on the left side, so in order
        #to equalize that imbalance, we need to pair it with another equal x-r imbalanc
        MOD=10**9 +7
        for x in nums:
            r = int(str(x)[::-1])
            off = x - r
            ans+=C[off]
            ans%=MOD
            C[off]+=1
            C[off]%=MOD
        return ans


        