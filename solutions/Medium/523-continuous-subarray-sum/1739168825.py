class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d,ssum={0:-1},0
        for i,x in  enumerate(nums):
            ssum+=x
            ssum%=k
            if ssum in d and i-d[ssum] >= 2: return True
            if ssum not in d: d[ssum] = i
        return False
        