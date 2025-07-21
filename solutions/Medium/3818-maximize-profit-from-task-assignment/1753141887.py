class Solution:
    def maxProfit(self, workers: List[int], tasks: List[List[int]]) -> int:
        C = Counter(workers)
        tasks.sort(key=lambda x: -x[1])
        ans = 0
        used = False
        for skill, reward in tasks:
            if C[skill] > 0:
                C[skill]-=1
                ans+=reward
            elif not used:
                used = True
                ans+=reward
        return ans
