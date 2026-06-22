class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:

        m = len(words)
        n = len(target)

        @cache
        def dp(i):
            if i == n:
                print("HIT")
                return 0

            best = 1e10
            for j in range(m):
                can = words[j]
                if i + len(can) <= n and target[i:i+len(can)] == can:
                    best = min(best, costs[j] + dp(i+len(can)))

            return best

        res = dp(0)
        return res if res < 1e10 else -1


        