class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:

        d = defaultdict(list)
        m = len(queries)
        out = [-1]*m
        for i in range(m):
            a,b = queries[i]
            j = max(a,b)
            if a == b:
                #edge case where neither person has to move buildings
                out[i] = a
            elif heights[min(a,b)] < heights[max(a,b)]:
                #edge case where only 1 person has to move buildings
                out[i] = max(a,b) 
            else:
                #both people have to move buildings -- enqueue for later
                d[j].append([i, max(heights[a], heights[b])])


        pq = []
        n = len(heights)
        for i in range(n):
            for idx,v in d[i]:
                heapq.heappush(pq, [v, idx])
            
            while pq and pq[0][0] < heights[i]:
                _, idx = heapq.heappop(pq)
                out[idx] = i
        return out