class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        seen = set()
        tables = set()
        C = Counter()
        for _, table, food in orders:
            table = int(table)
            seen.add(food)
            tables.add(table)
            C[(table, food)]+=1

        out = []
        header = []
        header.append("Table")
        for k in sorted(seen):
            header.append(k)

        out.append(header)
        for t in sorted(tables):
            tmp = [str(t)]
            for x in header[1:]:
                tmp.append(str(C[(t,x)]))
            out.append(tmp)
        return out
            
            
        
            