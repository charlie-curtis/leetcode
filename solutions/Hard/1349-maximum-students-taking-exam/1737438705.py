class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:

        m,n = len(seats),len(seats[0])
        perms = [[] for _ in range(m)]

        def bt(row, cur):
            nonlocal perms

            i = len(cur)
            if i == n:
                perms[row].append(tuple(cur))
                return
            c = seats[row][i]
            if c == '.' and (not cur or cur[-1] != 1):
                cur.append(1)
                bt(row, cur)
                cur.pop()
            
            cur.append(0)
            bt(row, cur)
            cur.pop()
            
        for i in range(m):
            bt(i, [])

        def good(now, prev):
            if prev == -1:
                return True
            n = len(now)
            for i in range(n):
                if now[i] != 1:
                    continue
                if i-1 >= 0 and prev[i-1] == 1:
                    return False
                if i+1 < n and prev[i+1] == 1:
                    return False
            return True
            
        @cache
        def dp(i,prev):
            if i == m:
                return 0

            ans = 0
            for p in perms[i]:
                cur = p.count(1)
                if good(p, prev):
                    ans = max(ans, dp(i+1, p) + cur)
            return ans

        return dp(0, -1)