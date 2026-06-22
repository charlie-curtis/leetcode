class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:

        m,n = len(mat), len(mat[0])

        def check():
            for i in range(m):
                for j in range(n):
                    if mat[i][j] != 0:
                        return False
            return True

        ans = 1e15
        def bt(cur, steps):
            if cur == m*n:
                if check():
                    nonlocal ans
                    ans = min(ans, steps)
                return

            #if we don't change anything
            bt(cur+1, steps)

            i = cur//n
            j = cur%n
            dirs = [[-1,0], [1,0], [0,1], [0,-1], [0,0]]
            nxt = [(i+x, j+y) for (x,y) in dirs]
            for ni, nj in nxt:
                if ni < 0 or nj < 0 or ni == m or nj == n:
                    continue
                mat[ni][nj] = 1-mat[ni][nj]
            bt(cur+1, steps+1)
            for ni, nj in nxt:
                if ni < 0 or nj < 0 or ni == m or nj == n:
                    continue
                mat[ni][nj] = 1-mat[ni][nj]
        
        bt(0,0)
        return ans if ans != 1e15 else -1
        