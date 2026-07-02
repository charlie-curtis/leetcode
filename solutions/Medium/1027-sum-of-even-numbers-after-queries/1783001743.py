class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        ssum = sum([x if not x%2 else 0 for x in nums]) 

        out = []
        for v, idx in queries:
            original = nums[idx]
            new = nums[idx] + v
            original_weight = 0 if original % 2 else original
            new_weight = 0 if new % 2 else new
            diff = new_weight - original_weight
            nums[idx] = new 
            ssum+=diff
            out.append(ssum)
        return out

        