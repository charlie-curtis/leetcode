class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        A = B = 0
        R = reduce(xor, nums) #will produce A^B after cancelling the other numbers
        T = R & -R #will find the lsb that is set (though any bit will do)

        for x in nums: #partition based on aforementioned bit. You'll be left with A^0 and B^0
            if x & T:
                A^=x
            else:
                B^=x
        return [A,B]