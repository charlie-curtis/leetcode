class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:


        p = permutations(strength)
        ans = 1e15
        for li in p:
            can = 0
            multi = 1
            for i in range(len(li)):
                a = li[i]
                b = multi 
                can+= ceil(a/b)
                multi+=k
            ans = min(can, ans)
        return ans