class Solution:
    def slowestKey(self, times: List[int], keys: str) -> str:

        best = 0
        ans = "a"

        n = len(times)
        for i in range(n):
            now = times[i]
            prev = 0 if i == 0 else times[i-1]
            if (now - prev > best) or (now - prev == best and ans < keys[i]):
                ans = keys[i]
                best = now-prev
        return ans
        