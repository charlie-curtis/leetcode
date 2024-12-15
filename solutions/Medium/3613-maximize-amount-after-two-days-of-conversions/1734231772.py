class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:


        m,n = len(pairs1), len(pairs2)
        graph1 = defaultdict(set)
        graph2 = defaultdict(set)

        for i in range(m):
            u,v = pairs1[i]
            r = rates1[i]
            graph1[u].add((v,r))
            graph1[v].add((u, 1/r))
            
        for i in range(n):
            u,v = pairs2[i]
            r = rates2[i]
            graph2[u].add((v,r))
            graph2[v].add((u, 1/r))


        ans = 1.0
        def bt(v, cur, seen):
            nonlocal ans
            #print("Day1", cur, v)

            if cur in seen:
                return
            seen.add(cur)

            if cur == initialCurrency:
                #print(v, cur, "day1")
                ans = max(v, ans)

            #we have two choices
            #1) go to one of our neighbors
            for nxt,r in graph1[cur]:
                bt(v*r, nxt, seen)
            #2) start day 2
            bt2(v, cur, set())


        def bt2(v, cur, seen):
            nonlocal ans
            #print("DAy2", cur, v)
            if cur in seen:
                return
            seen.add(cur)
            
            if cur == initialCurrency:
                #print(v, cur, "day2")
                ans = max(v, ans)

            #we have one choice
            #1) go to one of our neighbors
            for nxt,r in graph2[cur]:
                bt2(v*r, nxt, seen)



        bt(1.0, initialCurrency, set())
        return ans
        