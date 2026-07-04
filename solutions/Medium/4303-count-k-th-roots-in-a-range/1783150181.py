class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:

        #k=1
        if k==1:
            return r-l+1
        

        ans = 0
        for i in range(int(sqrt(r)) + 1):
            v = i**k
            if l <= v <= r:
                ans+=1
            if v > r:
                break
        return ans
        