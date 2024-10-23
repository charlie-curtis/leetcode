class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:

        n = len(colors)
        left_close = [[float('inf') for _ in range(3)] for _ in range(n)]
        right_close = [[float('inf') for _ in range(3)] for _ in range(n)]

        last_seen = [float('inf')]*3
        for i in range(n):
            c = colors[i]
            last_seen[c-1] = i

            for j in range(3):
                left_close[i][j] = last_seen[j]

        last_seen = [float('inf')]*3
        for i in range(n-1, -1, -1):
            c = colors[i]
            last_seen[c-1] = i

            for j in range(3):
                right_close[i][j] = last_seen[j]

        

        out = []
        for i, target in queries:
            lv = left_close[i][target-1]
            rv = right_close[i][target-1]

            a,b = abs(i - rv), abs(i - lv)
            out.append(min(a,b))
        
        return [x if x != float('inf') else -1 for x in out]


        