class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:

        #10011
        #01010

        #111000
        #000111

        #even + even = even
        #even + odd = odd -> because we can only reduce the number of bits by 2 each time
        #odd + odd = even

        #so if we didn't have 3 arrays, and only had 2, then
        #odd + odd number would produce an even set num of bits
        #and even + even would also do that

        #but now that we have 3 numbers, the question is like, "how many even/odd combinations can we make?"
        #so do operations on A&B First, then feed that output to C

        Aodd = len([x for x in a if x.bit_count() % 2])
        Aeven = len(a) - Aodd
        Bodd = len([x for x in b if x.bit_count() % 2])
        Beven = len(b) - Bodd
        Codd = len([x for x in c if x.bit_count() % 2])
        Ceven = len(c) - Codd

        Teven = Aeven*Beven + Aodd*Bodd
        Todd = Aeven*Bodd + Aodd*Beven

        ans = Teven*Ceven + Todd*Codd

        return ans



