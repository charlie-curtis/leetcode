from sortedcontainers import SortedList
class Solution:
    def countPairs(self, A: List[int], B: List[int]) -> int:

        n = len(A)

        sl = SortedList()
        ans = 0
        for i in range(n):
            diff = A[i] - B[i]
            ans+= len(sl) - sl.bisect_right(-diff)
            sl.add(diff)
        return ans


