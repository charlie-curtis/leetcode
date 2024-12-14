class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:

        d = defaultdict(set)
        in_degree = Counter({i:0 for i in range(1,len(nums)+1)})
        for li in sequences:
            n = len(li)
            for i in range(n-1):
                a,b = li[i], li[i+1]
                #directed edge from a -> b
                if b not in d[a]:
                    d[a].add(b)
                    in_degree[b]+=1

        q = deque()
        out = []
        for k,v in in_degree.items():
            if v == 0:
                q.append(k)


        while q:

            n = len(q)
            if n > 1:
                return False

            for i in range(n):
                a = q.popleft()
                out.append(a)
                for b in d[a]:
                    in_degree[b]-=1
                    if in_degree[b] == 0:
                        q.append(b)

        if sum(in_degree.values()) != 0:
            return False
        #print(out, nums)
        return out == nums
                

        