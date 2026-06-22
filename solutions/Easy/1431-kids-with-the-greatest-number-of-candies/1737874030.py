class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        out = []
        for i,x in enumerate(candies):
            candies[i]+=extraCandies
            C = Counter(candies)
            if max(C.keys()) == candies[i]:
                out.append(True)
            else:
                out.append(False)
            candies[i]-=extraCandies
        return out
        