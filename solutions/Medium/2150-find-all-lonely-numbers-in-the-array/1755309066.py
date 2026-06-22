class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        C = Counter(nums)
        ans = []
        for k in C.keys():
            if C[k-1] == 0 and C[k+1] == 0 and C[k] == 1:
                ans.append(k)
        return ans
        