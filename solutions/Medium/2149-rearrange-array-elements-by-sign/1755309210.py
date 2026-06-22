class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negs = [x for x in nums if x < 0]
        pos = [x for x in nums if x > 0]

        out = []
        for f,s in zip(pos, negs):
            out.append(f)
            out.append(s)
        return out


        