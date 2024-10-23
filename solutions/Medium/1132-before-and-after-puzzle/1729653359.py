class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:

        begins = defaultdict(list)
        for i,x in enumerate(phrases):
            whole = x.split(" ")
            first = whole[0]
            rest = "" if len(whole) == 1 else ' '.join(whole[1:])
            begins[first].append([i, rest])


        out = set()
        for i, x in enumerate(phrases):
            last = x.split(" ")[-1]
            for j, y in begins[last]:
                if i == j:
                    continue
                if y:
                    print(x,y)
                    out.add(x + " " +  y)
                else:
                    out.add(x)
        return sorted(out)