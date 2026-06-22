# Definition for BigArray.
# class BigArray:
#     def at(self, index: long) -> int:
#         pass
#     def size(self) -> long:
#         pass
class Solution(object):
    def countBlocks(self, nums: Optional['BigArray']) -> int:

        n = nums.size()
        def endpoint(l):
            r = n-1
            target = nums.at(l)
            #TTTTTTFFF
            while l <= r:
                mid = l + (r-l)//2
                if nums.at(mid) == target:
                    l = mid + 1
                else:
                    r = mid -1
            return r

        
        l = 0
        ans = 0
        while l != n:
            ans+=1
            l = endpoint(l) + 1
        
        return ans

        