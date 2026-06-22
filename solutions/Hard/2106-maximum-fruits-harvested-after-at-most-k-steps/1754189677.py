class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        #there is a 2 pointer approach to this. Binary search was fast enough for the given constraints
        locs = [x[0] for x in fruits]
        values = [x[1] for x in fruits]
        pre = list(accumulate(values, initial=0))
        n = len(fruits)

        def check_left_first():
            ans = 0
            idx = bisect_right(locs, startPos)-1
            original = idx
            cnt = 0
            while idx >= 0 and (startPos - locs[idx] <= k):
                cnt+=values[idx]
                rem = k - (startPos - locs[idx])
                other_idx = bisect_right(locs, rem+locs[idx]) -1
                if other_idx > original:
                    ans = max(ans, cnt + pre[other_idx+1] - pre[original+1])
                else:
                    ans = max(ans, cnt)
                idx-=1
            return ans

        def check_right_first():
            ans = 0
            idx = bisect_left(locs, startPos)
            original = idx
            cnt = 0
            while idx < n and (locs[idx] - startPos <= k):
                cnt+=values[idx]
                rem = k - (locs[idx] - startPos)
                other_idx = bisect_left(locs, locs[idx]-rem)
                if other_idx < original:
                    ans = max(ans, cnt + pre[original] - pre[other_idx])
                else:
                    ans = max(ans, cnt)
                idx+=1
            return ans

        a = check_right_first()
        b = check_left_first()
        #print(a,b)
        return max(a,b)

        