class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        dirs = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],

            [1,1],
            [-1,-1],
            [-1,1],
            [1,-1]
        ]

        Q = set()
        out = []
        for x,y in queens:
            Q.add((x,y))
        for i,j in dirs:
            x,y = king
            x+=i
            y+=j
            while 0 <= x < 8 and 0 <= y < 8:
                if (x,y) in Q:
                    out.append([x,y])
                    break
                x+=i
                y+=j
        return out


        