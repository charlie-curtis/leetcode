class Solution:
    def minimumSeconds(self, land: List[List[str]]) -> int:

        m, n = len(land), len(land[0])

        floods_to_process = []
        steps_to_process = []
        V = set()
        for i in range(m):
            for j in range(n):
                if land[i][j] == '*':
                    floods_to_process.append([i,j])
                    V.add((i,j))
                elif land[i][j] == 'S':
                    steps_to_process.append([i,j])
                    V.add((i,j))

        def invalid(i,j):
            return i < 0 or i == m or j < 0 or j == n or land[i][j] == 'X'
        def enqueue(i,j, holding_tank):
                dirs = [[1,0], [-1,0], [0,1], [0,-1]]

                for x,y in dirs:
                    if invalid(i+x, j+y):
                        continue
                    holding_tank.append([i+x, j+y])
                    

        t = 0
        while floods_to_process or steps_to_process:

            tmp_nxt_floods = []
            tmp_nxt_steps = []
            while floods_to_process:
                i,j = floods_to_process.pop()
                if land[i][j] == 'D':
                    continue
                enqueue(i,j, tmp_nxt_floods)
            
            while steps_to_process:
                i,j = steps_to_process.pop()
                if land[i][j] == 'D':
                    return t
                enqueue(i,j, tmp_nxt_steps)

            for x,y in tmp_nxt_floods:
                tup = (x,y)
                if tup in V or land[x][y] == 'D':
                    continue
                V.add(tup)
                floods_to_process.append([x,y])

            for x,y in tmp_nxt_steps:
                tup = (x,y)
                if tup in V:
                    continue
                V.add(tup)
                steps_to_process.append([x,y])

            #print(V)
            #print("nxt steps", steps_to_process)
            #print("nxt floods", floods_to_process)

            t+=1
        return -1