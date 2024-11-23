from sortedcontainers import SortedDict
class Solution:
    def maxDepthBST(self, order: List[int]) -> int:


        sd = SortedDict()
        ans = 0
        #this problem was hard and i had to rely on the editorial. The key observation that I missed is that when inserting elements, we can look at our neighbors just greater or just less than and see what their depth is and base our answer off of that.
        for x in order:
            depth = 1
            idx1 = sd.bisect_left(x)-1
            idx2 = sd.bisect_left(x)
            if idx1 != -1:
                depth = 1 + sd.peekitem(idx1)[1]
            if idx2 != len(sd):
                depth = max(depth, 1 + sd.peekitem(idx2)[1])

            sd[x] = depth
            ans = max(ans, depth)

        return ans


            

