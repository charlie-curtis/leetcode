class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:


        d = defaultdict(list)

        n = len(username)
        for i in range(n):
            user = username[i]
            t = timestamp[i]
            site = website[i]

            d[user].append([t, site])

        best = 0
        ans = ""

        triples = {}
        for li in d.values():
            singles = set()
            doubles = set()
            seen = set()
            li.sort()
            for _, site in li:
                #setup triples
                for k in doubles:
                    s = k + ':' + site
                    if s in seen:
                        continue
                    seen.add(s)
                    if s in triples:
                        triples[s]+=1
                    else:
                        triples[s] = 1
                    if (triples[s] > best) or (triples[s] == best and s < ans):
                        best = triples[s]
                        ans = s
                for k in singles:
                    s = k + ':' + site
                    doubles.add(s)
                singles.add(site)
        return ans.split(':')
                
