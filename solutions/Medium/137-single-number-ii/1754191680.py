class Solution:
    def singleNumber(self, nums: List[int]) -> int:


        #every bit, mod 3, should be 0. If it is mod 1, then it's set in the answer

        #10
        #10
        #11
        #10

        bits = Counter()
        ans = 0
        for i in range(32):
            bits = 0
            for x in nums:
                bits+= (abs(x)>>i)&1
            if bits % 3 != 0:
                ans+=(1<<i)
        
        return ans if nums.count(ans) == 1 else -ans
