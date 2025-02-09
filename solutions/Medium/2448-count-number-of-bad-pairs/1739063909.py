class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        C = Counter()
        n = len(nums)
        T = (n-1)*n//2

        for i,x in enumerate(nums):
            C[x-i]+=1
        

        for v in C.values():
            v-=1
            T-=(v)*(v+1)//2
        return T

        