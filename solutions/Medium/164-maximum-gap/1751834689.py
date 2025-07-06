class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        width = ((max(nums) - min(nums)) // (n-1))
        width = max(width, 1)

        H = {}
        for x in nums:
            b = x//width
            b*=width
            if b not in H:
                H[b] = [x,x]
            else:
                H[b] = [min(H[b][0], x), max(H[b][1], x)]
            
        
        last = -1
        ans = 0
        start = min(H.keys())
        end = max(H.keys())
        for i in range(start, end+1, width):
            if i not in H:
                continue
            small, large = H[i]
            #ans = max(ans, large-small)
            if last != -1:
                ans = max(ans, small-last)
            last = large
        return ans
            

        


        #1 5 9 13

        #n = 4
        #(13-1)/(3) = 4
        
        