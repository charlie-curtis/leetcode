class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        if n == 1:
            return 1


        in_degree = Counter()
        for i in range(n):
            in_degree[i] = 0
        
        d = defaultdict(set)
        for u,v in edges:
            in_degree[u]+=1
            in_degree[v]+=1
            d[u].add(v)
            d[v].add(u)


        ans = 0
        q = deque()
        for t,v in in_degree.items():
            if v == 1:
                q.append(t)
        

        #print(q)
        seen = set()
        #print(values, k)
        while q:
            #print(values)
            v = q.popleft()
            #print("processing", v)

            if v in seen:
                continue
            seen.add(v)
            
            if values[v] % k == 0:
                values[v] = 0
                ans+=1
                #print("adding for node", v)
            else:
                pass
                #print("I am not eligible, k is", k, "but i was", values[v])

            if len(d[v]) > 1:
                raise ValueError("idk what i'm doing")
            for u in d[v]:
                d[u].remove(v)
                if values[v] > 0:
                    #print("transfering my power from", v, "to", u)
                    values[u]+=values[v]
                    values[v] = 0
                in_degree[u]-=1
                if in_degree[u] == 1:
                    q.append(u)
        return ans