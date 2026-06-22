class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        set_guards = set()
        for x,y in guards:
            set_guards.add((x,y))
        set_walls = set()
        for x,y in walls:
            set_walls.add((x,y))

        ans = [[True for _ in range(n)] for _ in range(m)]
        #go from l to r
        for i in range(m):
            lastSeen = None
            for j in range(n):
                t = (i,j)
                if t in set_guards:
                    lastSeen = 'g'
                if t in set_walls:
                    lastSeen = 'w'
                if lastSeen == 'g' or t in set_walls:
                    ans[i][j] = False

        # go from r to l
        for i in range(m):
            lastSeen = None
            for j in range(n-1, -1, -1):
                t = (i,j)
                if t in set_guards:
                    lastSeen = 'g'
                if t in set_walls:
                    lastSeen = 'w'
                if lastSeen == 'g' or t in set_walls:
                    ans[i][j] = False

        # go from top to bottom 
        for i in range(n):
            lastSeen = None
            for j in range(m):
                t = (j,i)
                if t in set_guards:
                    lastSeen = 'g'
                if t in set_walls:
                    lastSeen = 'w'
                if lastSeen == 'g' or t in set_walls:
                    ans[j][i] = False

        #go from bottom to top
        for i in range(n):
            lastSeen = None
            for j in range(m-1, -1, -1):
                t = (j,i)
                if t in set_guards:
                    lastSeen = 'g'
                if t in set_walls:
                    lastSeen = 'w'
                if lastSeen == 'g' or t in set_walls:
                    ans[j][i] = False

        out = 0
        for i in range(m):
            for j in range(n):
                if ans[i][j] == True:
                    out+=1
        return out
        