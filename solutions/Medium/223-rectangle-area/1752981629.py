class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:



        leftx = max(ax1,bx1)
        rightx = min(ax2,bx2)
        bottomy = max(by1, ay1)
        topy = min(ay2, by2)

        overlap = 0
        if bottomy <= topy and leftx <= rightx:
            overlap = (topy - bottomy) * (rightx - leftx)

        return (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1) - overlap
         