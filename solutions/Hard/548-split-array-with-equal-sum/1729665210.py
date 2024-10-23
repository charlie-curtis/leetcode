class Solution:
    def splitArray(self, nums: List[int]) -> bool:


        def check(i, j, target):
            if j-i+1 < 3:
                return False

            cur = nums[i]
            rem = sum(nums[i:j+1]) - cur


            for k in range(i+1,j):
                rem-=nums[k]
                if cur == rem == target:
                    return True
                cur+=nums[k]
            return False


        suff = defaultdict(set)
        n = len(nums)
        cur = nums[-1]
        for i in range(n-2,-1,-1):
            suff[cur].add(i)
            cur+=nums[i]


        cur = nums[0]
        for i in range(1,n):
            for j in suff[cur]:
                if j > i and check(i+1, j-1, cur):
                    return True
            cur+=nums[i]
        return False
