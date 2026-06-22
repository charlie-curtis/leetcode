class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:

        target = list(set(target))
        n = len(nums)
        m = len(target)
        @cache
        def dp(i,state):
            if state == 2**m - 1:
                return 0
            if i == n:
                return 1e15


            ans = dp(i+1, state)
            x = nums[i]
            for j in range(m):
                if state&(1<<j) > 0:
                    continue
                t = target[j]
                newx = x
                if t >= x:
                    #print("incrementing", x, "to ", t)
                    newx = t
                    b = t-x
                else:
                    d = ceil(x/t)
                    b = (d*t) - x
                    newx = d*t
                    #print("target", t, "me", x, "going for", d*t)

                tmpstate = state
                for l in range(m):
                    if state&(1<<l) == 0 and newx % target[l] == 0:
                        tmpstate|=(1<<l)
                c = dp(i+1, tmpstate) + b
                ans = min(ans, c)

            return ans



        return dp(0,0)
        