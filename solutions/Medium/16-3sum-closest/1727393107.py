class Solution:
    def threeSumClosest(self, A: List[int], target: int) -> int:

        A.sort()
        ans = best_diff = 1e10 
        n = len(A)
        def go(i, target):
            nonlocal ans, best_diff
            l, r = i+1, n-1
            while l < r:
                ssum = A[l] + A[r] + A[i]
            
                if abs(target-ssum) <= best_diff:
                    ans = ssum
                    best_diff = abs(target-ssum)
                if ssum > target:
                    r-=1
                else:
                    l+=1
            return ans
        for i in range(n-2):
            candidate = go(i, target)
        return ans

        