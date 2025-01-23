class Solution:
    def minJumps(self, arr: List[int]) -> int:


        q = deque()
        q.append([0,0])


        adj = defaultdict(list)
        for i,x in enumerate(arr):
            adj[x].append(i)
        n = len(arr)

        seen = set()
        seen.add(0)

        while q:
            idx, cost = q.popleft()

            if idx == n-1:
                return cost

            li = adj[arr[idx]]

            while li:
                q.append([li.pop(), cost+1])

            if idx -1 >=0 and idx-1 not in seen:
                seen.add(idx-1)
                q.append([idx-1, cost+1])
            if idx+1 < n and idx+1 not in seen:
                seen.add(idx+1)
                q.append([idx+1, cost+1])

        return -1

            
        