class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        li = sorted(set(arr))
        d = {}
        for i,x in enumerate(li):
            d[x] = i+1

        return [d[x] for x in arr]
            
        