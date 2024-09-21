class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []

        ans = []
        n = len(nums)
        cur = []

        for i in range(n):
            if not cur:
                cur = [nums[i]]
                expected = nums[i]+1
            elif nums[i] != expected:
                cur.append(expected-1)
                ans.append(cur.copy())
                cur = [nums[i]]
                expected = nums[i]+1
            else:
                expected+=1
        
        cur.append(expected-1)
        ans.append(cur.copy())

        return [str(x[1])  if x[0] == x[1] else str(x[0]) + "->" + str(x[1]) for x in ans]

        