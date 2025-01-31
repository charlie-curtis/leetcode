class Solution:
    def isPathCrossing(self, path: str) -> bool:

        seen = set()

        x,y = 0, 0
        seen.add((x,y))
        for c in path:
            if c == 'E':
                x+=1
            elif c == 'W':
                x-=1
            elif c == 'S':
                y-=1
            else:
                y+=1

            if (x,y) in seen:
                return True
            seen.add((x,y))
        print(seen)
        return False
        