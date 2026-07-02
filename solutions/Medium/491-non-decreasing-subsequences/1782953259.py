class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        out=set()
        n=len(nums)
        
        def bt(i,cur):
            if i==n:
                if len(cur)>=2:
                    out.add(tuple(cur))
                return
            
            if not cur or cur[-1] <= nums[i]:
                cur.append(nums[i])
                bt(i+1, cur)
                cur.pop()
            bt(i+1, cur)
        bt(0, [])
        return list(out)