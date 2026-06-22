class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:

        n = len(nums)
        MOD = 10**9 + 7
        cur = 0
        C = Counter()

        def add_ele(val, cur):
            cur_freq = C[val]
            if cur_freq > 0:
                cur-=pow(val, cur_freq, MOD)
            C[val]+=1
            cur_freq = C[val]
            cur+=pow(val, cur_freq, MOD)
            cur%=MOD
            return cur
        def remove_ele(val, cur):
            cur_freq = C[val]
            cur-=pow(val, cur_freq, MOD)
            C[val]-=1
            cur_freq = C[val]
            if cur_freq > 0:
                cur+=pow(val, cur_freq, MOD)
            cur%=MOD
            return cur

        j = 0
        ans = 0
        for i in range(n):
            cur = add_ele(nums[i], cur)

            if i-j+1 > k:
                cur = remove_ele(nums[j], cur)
                j+=1
            
            if i-j+1 == k:
                ans = max(ans, cur)
        return ans





        