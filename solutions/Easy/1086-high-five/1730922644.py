class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        n = len(items)
        d = defaultdict(list)

        for id, score in items:
            li = d[id]
            li.append(score)
            li = sorted(li, reverse=True)[:min(5, len(li))]
            d[id] = li
        
        out = []
        for id in sorted(d.keys()):
            li = d[id]
            out.append([id, sum(li) // len(li)])
        return out