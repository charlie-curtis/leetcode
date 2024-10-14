class Solution:
    def canMeasureWater(self, x_cap: int, y_cap: int, target: int) -> bool:


        q = [[0,0]]
        seen = set()

        while q:
            x,y = q.pop()

            if (x,y) in seen:
                continue
            if x+y == target:
                return True
            
            seen.add((x,y))

            #fill x
            q.append([x_cap, y])
            #fill y
            q.append([x, y_cap])
            #dump y into x
            rem = x_cap-x
            chosen = min(y, rem)
            q.append([x+chosen, y-chosen])
            #dump x into y
            rem = y_cap-y
            chosen = min(x, rem)
            q.append([x-chosen, y+chosen])
            #clear x
            q.append([0, y])
            #clear y
            q.append([x,0])
        return False


        