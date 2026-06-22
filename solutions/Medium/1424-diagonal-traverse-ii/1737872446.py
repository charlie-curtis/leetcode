class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        d = defaultdict(list)
        m,n = len(nums), len(nums[0])
        print(nums)
        for i in range(m):
            n = len(nums[i])
            for j in range(n):
                d[i+j].append(nums[i][j])

        out = []
        for k in sorted(d.keys()):
            out+=d[k][::-1]
        return out
        