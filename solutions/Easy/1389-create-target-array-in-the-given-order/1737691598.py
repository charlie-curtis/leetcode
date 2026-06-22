class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        out = []
        for idx, v in zip(index, nums):
            if idx == len(out):
                out.append(v)
            else:
                out.insert(idx, v)
        return out
        