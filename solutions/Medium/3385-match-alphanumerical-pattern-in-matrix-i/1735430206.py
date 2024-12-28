class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:


        m,n = len(board), len(board[0])
        m2, n2 = len(pattern), len(pattern[0])


        def check(off1,off2):
            mmap = {}
            rmap = {}
            for i in range(m2):
                if i + off1 >= m:
                    return False
                for j in range(n2):
                    if j + off2 >= n:
                        return False

                    a = pattern[i][j]
                    b = str(board[i+off1][j+off2])

                    if not a.isalpha():
                        if a != b:
                            return False
                        continue
            
                    #else we are mapping something like 3 -> a
                    if a in mmap:
                        if b not in rmap:
                            return False
                        if mmap[a] != b or rmap[b] != a:
                            return False
                    elif b in rmap:
                        return False

                    mmap[a] = b
                    rmap[b] = a
            return True

        for i in range(m):
            for j in range(n):
                if check(i,j):
                    return [i,j]
        return [-1, -1]