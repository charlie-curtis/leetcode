class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        T = []
        for x,y in points:
            T.append([sqrt(x**2 + y**2), [x,y]])

        T.sort()
        P = T[:k]
        return [x for _,x in P]
        