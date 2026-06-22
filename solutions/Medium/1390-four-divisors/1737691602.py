class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def count(y):
            x = 1
            cnt = 0
            out = set()
            while x*x <= y:
                if y % x == 0:
                    out.add(x)
                    out.add(y//x)
                x+=1
            
            return out


        
        ans = 0
        for x in nums:
            seen = count(x)
            if len(seen) == 4:
                ans+=sum([x for x in seen])
        return ans
        