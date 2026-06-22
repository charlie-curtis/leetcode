class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        n = len(arr)

        @cache
        def dp(i):
            ans = 0
            for j in range(i+1,n):
                if j > i+d or arr[i] <= arr[j]:
                    break
                ans = max(ans, 1 + dp(j))
            for j in range(i-1, -1, -1):
                if j < i - d or arr[i] <= arr[j]:
                    break
                ans = max(ans, 1 + dp(j))
            return ans

        ans = max([dp(i) for i in range(n)])
        return ans+1
