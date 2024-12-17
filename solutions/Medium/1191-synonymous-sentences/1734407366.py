class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:

        edges = defaultdict(set)
        for u,v in synonyms:
            edges[u].add(v)
            edges[v].add(u)

        
        words = text.split(" ")

        d = defaultdict(set)
        def bt(cur, original):

            if cur in d[original]:
                return
            
            d[original].add(cur)

            for u in edges[cur]:
                bt(u, original)



        for x in words:
            bt(x,x)

        n = len(words)
        ans = []
        def bt2(i, cur):
            if i == n:
                ans.append(' '.join(cur))
                return


            original = words[i]
            for u in d[original]:
                cur.append(u)
                bt2(i+1,cur)
                cur.pop()

        bt2(0, []) 
        return sorted(ans)