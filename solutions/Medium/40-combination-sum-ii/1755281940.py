class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        seen = set()

        def bt(cur,i,ssum):
            h = hash(tuple(cur))
            if (h,i,ssum) in seen:
                return
            seen.add((h,i,ssum))
            if ssum == target:
                ans.add(tuple(cur.copy()))
                return
            if ssum > target or i == len(candidates):
                return
            
            bt(cur, i+1, ssum)
            cur.append(candidates[i])
            bt(cur, i+1, ssum+candidates[i])
            cur.pop()
        

        bt([], 0, 0)
        return [list(x) for x in ans]
        