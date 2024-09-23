from sortedcontainers import SortedList
class Solution:
    def threeSumSmaller(self, A: List[int], target: int) -> int:

        def twoSumSmaller(idx, target):
            l = idx
            r = n-1
            ans = 0
            while r > l:
                ssum = A[l] + A[r]
                if ssum < target:
                    ans+= r -l
                    l+=1
                else:
                    r-=1
            return ans

        n = len(A)
        A.sort()
        l, r = 0, n-1
        ans = 0
        for i in range(n):
            res = twoSumSmaller(i+1, target - A[i])
            ans+=res
        return ans


