class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:

        def lis(keep):
            cur = []
            for x in nums:
                if x&keep == 0:
                    continue
                idx = bisect_left(cur, x)
                if idx == len(cur):
                    cur.append(x)
                else:
                    cur[idx] = x

            return len(cur)

        return max([lis(1<<x) for x in range(32)])