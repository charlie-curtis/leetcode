class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:


        ans = []
        ranges.sort()

        cur = []
        expected = 0
        for start,end in ranges:
            if expected < start:
                ans.append([expected, start-1])
            expected = max(expected, end+1)

        if expected != n:
            ans.append([expected, n-1])
        return ans



        #[0, 7], [2,3], [9,11]

        