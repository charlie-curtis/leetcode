class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:

        #there is a well known formula for computing whether a set of points is convex. We basically
        #need to check the orientation for all 3 points. If all 3 points have the same orientation = convex

        n = len(points)
        def orient(i):
            x1,y1 = points[i%n]
            x2,y2 = points[(i+1)%n]
            x3,y3 = points[(i+2)%n]

            a = (y2-y1)*(x3-x2)
            b = (y3-y2)*(x2-x1)

            if a == b:
                return 0
            if a > b:
                return 1
            return -1





        A = [orient(i) for i in range(n) if orient(i) != 0]

        return len(set(A)) == 1