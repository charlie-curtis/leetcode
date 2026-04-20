class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:

        if len(set(beans)) == 1:
            return 0

        beans.sort()
        n = len(beans)
        A = list(accumulate(beans, initial = 0))

        ans = A[-1]
        for i in range(n):
            ans = min(ans, A[-1] - beans[i]*(n-i))
        return ans