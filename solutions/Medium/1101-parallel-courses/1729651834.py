class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        edges = defaultdict(set)
        cnts = Counter()
        for a,b in relations:
            edges[a].add(b)
            cnts[b]+=1

        q = deque()
        for i in range(1,n+1):
            v = cnts[i]
            if v == 0:
                q.append(i)

        ans = 0
        while q:
            ans+=1

            n = len(q)
            for i in range(n):
                a = q.popleft()
                for nxt in edges[a]:
                    cnts[nxt]-=1
                    if cnts[nxt] == 0:
                        q.append(nxt)


        #print(cnts)
        return ans if sum(cnts.values()) == 0 else -1