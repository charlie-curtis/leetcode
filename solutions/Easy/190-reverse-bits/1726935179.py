class Solution:
    def reverseBits(self, n: int) -> int:


        ans = 0
        multi = 1
        for i in range(32):
            bit = n % 2
            ans+= bit*2**(31-i)
            n//=2
        return ans