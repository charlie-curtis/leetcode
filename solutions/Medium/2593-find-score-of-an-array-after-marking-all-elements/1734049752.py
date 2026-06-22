class Solution:
    def findScore(self, nums: List[int]) -> int:

        q = [(x,i) for i,x in enumerate(nums)]
        marked = set()
        q.sort()
        score = 0

        for val, idx in q:
            if idx in marked:
                continue
            marked.add(idx-1)
            marked.add(idx)
            marked.add(idx+1)
            score+=val
        return score
        