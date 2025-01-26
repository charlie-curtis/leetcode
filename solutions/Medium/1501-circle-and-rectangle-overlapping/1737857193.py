class Solution:
    def checkOverlap(self, R: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:


        #I originally solved this by binary searching for the closest point on each side of the rectangle. Looking at solutions, there was a simpler approach

        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True


        def isgood(x1,y1):
            a = (x1-xCenter)**2
            b = (y1-yCenter)**2

            print(a,b, R**2)
            return a + b <= R**2

        xC = min(x2, max(x1, xCenter))
        yC = min(y2, max(y1, yCenter))

        return isgood(xC, y1) or isgood(xC, y2) or isgood(x1,yC) or isgood(x2, yC)


