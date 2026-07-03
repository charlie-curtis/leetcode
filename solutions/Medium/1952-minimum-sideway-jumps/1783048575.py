class Solution:
    def minSideJumps(self, blocks: List[int]) -> int:

        n = len(blocks)
        if n == 1:
            return 1

        prev = [10**9]*4
        cur = [10**9]*4
        for i in range(n-1, -1, -1):
            for lane in range(1,4):
                if i == n-1:
                    cur[lane] = (0 if blocks[i] != lane else 1)
                elif blocks[i] == lane:
                    cur[lane] = 10**9
                else:
                    a = prev[lane] # don't switch lanes
                    b = float('inf')
                    for lane2 in range(1,4):
                        if lane2 == lane or blocks[i] == lane2:
                            #if we are already in the lane or the lane is currently blocked, can't switch from it
                            continue
                        b = min(1 + prev[lane2], b)
                    cur[lane] = min(a,b)

            prev = cur
        
        return cur[2]