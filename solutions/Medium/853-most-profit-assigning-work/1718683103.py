class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        worker.sort(reverse=True)
        pairs = []

        for i in range(len(difficulty)):
            pairs.append([profit[i], difficulty[i]])


        ptr = 0
        ans = 0
        pairs.sort(reverse=True)
        for x in worker:
            while ptr < len(pairs) and pairs[ptr][1] > x:
                ptr+=1
            if ptr < len(pairs):
                ans+=pairs[ptr][0]
        return ans

        