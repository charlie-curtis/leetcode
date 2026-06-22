class Solution:
    def xorBeauty(self, nums: List[int]) -> int:

        #general idea: For each bit position, iterate over the array. For a given index, i, determine
        #if it contributes an even number or odd number for that bit position. Sum alll the contributions. If odd, it'll contribute to the final answer for that bit position.
        C = Counter()
        for i in range(32):
            for x in nums:
                if x&(1<<i) > 0:
                    C[i]+=1
        ans = 0
        #001
        #100
        for i in range(32):
            bit = 0
            for x in nums:
                if x & (1<<i) == 0:
                    continue
                n = C[i]
                #n! / ((n-1)!) = n
                #result = math.comb(n, 1) % 2
                bit^=(n%2)
            if bit:
                ans|=(1<<i)
        return ans
        