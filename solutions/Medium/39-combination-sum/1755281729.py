class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def bt(cur,i,ssum):
            if ssum == target:
                ans.append(cur.copy())
                return
            if ssum > target or i == len(candidates):
                return
            
            bt(cur, i+1, ssum)
            cur.append(candidates[i])
            bt(cur, i, ssum+candidates[i])
            cur.pop()
        

        bt([], 0, 0)
        return ans
        