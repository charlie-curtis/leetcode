class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        m = len(strs)
        n = len(strs[0])
        overall_state = [1] + [0]*(m-1)

        #strictly increasing -> the col is good and all the remaining cols
        #decreasing at all -> delete row unless i-1 was good

        ans = 0
        groups = [strs]
        for j in range(n): #(O(N))
            nxt_groups = []
            #if we are in a group, that means we're not strictly greater than yet
            #["abx","agz","bgc","bfc"] -> after processing 1 iteration, there would be 2 groups, [['abx', 'agz],  ['bgc', 'bfc']]
            good = True
            for g in groups: #[abx, agz]. #len(groups) * len(g) = M
                cur = []
                for x in g: #abx
                    if not cur or cur[-1][j] < x[j]:
                        #if this is strictly greater than the character before it, make a new group for next iteration
                        nxt_groups.append(cur.copy())
                        cur = [x]
                    elif cur[-1][j] == x[j]:
                        #else if its equal, keep it in the same group for next iteration
                        cur.append(x)
                    else:
                        #else we need to toss the column. This means they were equal until this point
                        #we are throwing this entire column away
                        good = False
                        break
                if not good: break
                nxt_groups.append(cur.copy())
            if good:
                groups = nxt_groups
            else:
                nxt_groups = groups
                ans+=1


        return ans
        