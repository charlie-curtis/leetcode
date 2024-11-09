class Solution:
    def minEnd(self, n: int, x: int) -> int:


        #the bits in x are fixed, so if x has a binary representation of 10011, the ones are fixed, and the 0s are flexible.
        #we can make up to 4 numbers with the 0s that are in x, so if n == 3 for example, we can make up to 4 numbers with the 0s in x. If n > 4, then we have to
        #prepend bits to the answer. If n=3, we could change the zeros in x to be 00, 01, 10 (and therefore the max would be 11011)

        ans = x

        found = 0
        #print(bin(x))
        for i in range(100):
            if x&(1<<i) == 0: #find the 0 bits
                bit = 1 if (1<<found)&(n-1) > 0 else 0
                ans|=(bit<<i) #set the 0 bits to the binary representation of n-1
                #print("setting the", i, "bit to", bit)
                found+=1 #note that we found a 0 bit

            #print("Found is", found)
            if 2**found >= n:
                break

        return ans