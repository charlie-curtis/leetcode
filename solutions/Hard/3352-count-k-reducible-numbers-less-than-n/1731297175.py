#Upsolved from the contest
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:

        M = 10**9 + 7
        @cache
        def reduce_count(bits):
            if bits == 1:
                return 0
            return reduce_count(bits.bit_count()) + 1

        n = len(s)
        @cache
        def compute(i, bits, flipped):
            if i == n:
                return 1 if bits > 0 and flipped and reduce_count(bits)+1 <= k else 0
        
            ans = 0
            if s[i] == '1':
                #let's say we flipped this bit (regardless of whether it was already flipped)
                ans+=compute(i+1, bits, True) % M
                #let's say we didn't flip this bit
                ans+=compute(i+1, bits+1, flipped) % M
            else:
                #this is a 0
                ans+=compute(i+1, bits, flipped) % M
                if flipped:
                    #simulate switching this to a 1
                    ans+=compute(i+1, bits+1, flipped) % M
                
            return ans % M

        return compute(0, 0, False)


        # 7 -> 3 -> 2 -> 1
        #111 is 7, so it becomes 3
        #011 is 3, so it becomes 2
        #010 is 2, so it becomes 1
        