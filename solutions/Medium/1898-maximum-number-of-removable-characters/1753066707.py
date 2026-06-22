class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        marked = {}
        for i,x in enumerate(removable):
            marked[x]  = i

        def check(skip):

            j = 0
            for i,x in enumerate(s):
                if i in marked and marked[i] <= skip:
                    continue
                if p[j] == x:
                    j+=1
                if j == len(p):
                    return True
            return False


        l = 0
        r = len(removable)

        #TTFFFFF
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return min(l, len(removable))
        