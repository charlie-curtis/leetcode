class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:


        n = len(toppingCosts)
        ans = float('inf')
        def check(base):
            nonlocal ans
            dist = abs(base-target)
            best_dist = abs(ans-target)

            if dist < best_dist or (dist == best_dist and base < ans):
                ans = base
        def solve(base, top_idx):
            if top_idx == n:
                return
            
            amt = toppingCosts[top_idx]
            check(base)
            check(base+amt)
            check(base+2*amt)

            solve(base, top_idx+1)
            solve(base+amt, top_idx+1)
            solve(base+2*amt, top_idx+1)
            

        for x in baseCosts:
            solve(x, 0)

        return ans
