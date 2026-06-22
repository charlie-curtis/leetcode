# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', tr: 'Point', bl: 'Point') -> int:


        '''
        x1,y2    x2,y2


        x1,y1.   x2,y1
        '''

        seen = set()

        x1,y1 = bl.x, bl.y
        x2,y2 = tr.x,tr.y

        cnt = 0
        def count(x1,y1, x2,y2):
            if x1 > x2 or y1 > y2:
                return
            s1 = (y2-y1)*(x2-x1)
            if not sea.hasShips(Point(x2,y2), Point(x1,y1)):
                return
            if x1 == x2 and y1 == y2:
                seen.add((x1,y1))
                return
            #divide into 4 regions UNLESS
            #x1 = x2 -> in this case, divide into top and bottom
            #y1 = y2 -> in this case, divide into left and right
            xMid = (x2-x1)//2 + x1
            yMid = (y2-y1)//2 + y1
            if x1 == x2:
                count(x1,y1,x1,yMid)
                count(x1,yMid+1, x1,y2)
                return
            if y1 == y2:
                #print("split into 2 regions vertically")
                count(x1,y1, xMid, y1)
                count(xMid+1,y1, x2, y1)
                return

            #x1 -> xMid,y1,ymid
            #x1 -> xMid,yMid+1,y2
            #xMId+1->x2, y1 -> yMid
            #xMId+1->x2, yMid+1, y2
            #print("split into 4 regions")
            count(x1,y1, xMid, yMid)
            count(x1,yMid+1, xMid, y2)
            count(xMid+1,y1, x2,yMid)
            count(xMid+1,yMid+1, x2,y2)
        count(x1,y1,x2,y2)
        return len(seen)