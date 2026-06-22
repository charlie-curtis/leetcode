class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        m = int(median(nums))

        def is_pali(x):
            original = x
            can = 0
            while x > 0:
                can*=10
                can+= (x%10)
                x//=10
            return can == original
        
        cans = set()
        t = m
        while not is_pali(t) and t < 10**9:
            t+=1
        if t != 10**9:
            cans.add(t)
        
        t = m
        while not is_pali(t) and t > 0:
            t-=1
        cans.add(t)

        
        def get_best(x):
            return sum([abs(x-y) for y in nums])
        
        return min([get_best(x) for x in cans])



