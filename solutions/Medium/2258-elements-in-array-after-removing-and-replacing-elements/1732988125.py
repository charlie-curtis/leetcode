class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        n = len(nums)

        first = [[i,n-1] for i in range(n)]
        second = [[0,i] for i in range(n-1)]

        whole = first + [[1e10, -1e10]] + second
        out = []
        m = len(whole)
        for t, j in queries:

            i = t%m

            start,end = whole[i]
            if start+j <= end:
                out.append(nums[start+j])
            else:
                out.append(-1)


        return out

        