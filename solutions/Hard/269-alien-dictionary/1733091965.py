class Solution:
    def alienOrder(self, words: List[str]) -> str:

        in_degree = Counter({c:0 for word in words for c in word})

        n = len(words)
        edges = defaultdict(set)

        def evalWords(w1,w2):
            j = 0
            while j < len(w1) and j < len(w2):
                if w1[j] != w2[j]:
                    a,b = w1[j], w2[j]
                    if b not in edges[a]:
                        in_degree[b]+=1
                        edges[a].add(b)
                    return
                j+=1

        for i in range(n-1):
            w1, w2 = words[i], words[i+1]
            if w2 == w1:
                #nothing to learn from this
                continue
            if w1.find(w2) == 0:
                #this is an edge case. If we get some input like abcd vs abc, then it can't be valid
                return ""
            evalWords(w1,w2)

        q = deque()
        for k,v in in_degree.items():
            if v == 0:
                q.append(k)

        ans = ""
        #print(in_degree)
        while q:
            letter = q.popleft()
            ans+=letter
            for u in edges[letter]:
                in_degree[u]-=1
                if in_degree[u] == 0:
                    q.append(u)

        #print(in_degree)
        if sum(in_degree.values()) != 0:
            return ""
        return ans