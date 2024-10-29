class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:



        #ttttffff

        l = -(10**4)**2
        r = (10**4)**2

        def check(mid):

            cur = 0
            seen = [0]*len(nums) #holds the lowest_pref seen at this index or any index to the left
            for i,x in enumerate(nums):
                cur+=x-mid #cur is a pref
                if i+1 >= k:
                    small_pref = seen[i-k] if i-k >= 0 else 0
                    if cur - small_pref >= 0:
                        return True
                
                #the smallest pref at this idx is either a previous pref, the current pref or starting over (x)
                seen[i] = min(cur, seen[i-1] if i > 0 else cur, 0)

            return False




        while r - l > 10**(-5):

            mid = l + (r-l)/2
            if check(mid):
                l = mid
            else:
                r = mid
        
        return r

