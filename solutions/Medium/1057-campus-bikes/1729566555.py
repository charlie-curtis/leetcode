class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:


        queues = []

        n,m = len(workers), len(bikes)
        d = defaultdict(list)
        for i,w in enumerate(workers):
            for j,b in enumerate(bikes):
                dst = abs(w[0] - b[0]) + abs(w[1] - b[1])
                d[dst].append([i,j])

        ans = [-1]*n

        seen_bikes = set()
        seen_workers = set()

        mmax = max(d.keys())
        while len(seen_workers) < n:

            for i in range(0, mmax+1):

                for worker, bike in d[i]:
                    if worker in seen_workers or bike in seen_bikes:
                        continue
                    
                    ans[worker] = bike
                    seen_bikes.add(bike)
                    seen_workers.add(worker)
        
        return ans