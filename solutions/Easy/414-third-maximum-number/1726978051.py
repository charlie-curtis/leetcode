class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        l = []
        for x in nums:
            if x in l:
                continue
            
            l.append(x)
            l.sort(reverse=True)
            if len(l) > 3:
                l = l[:3]
        return l[2] if len(l) == 3 else l[0]
