class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        C = Counter(text)

        ans = 1e9
        for x in 'balon':
            if x in 'lo':
                ans = min(C[x]//2, ans)
            else:
                ans = min(C[x], ans)
        return ans

        