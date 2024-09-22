class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def hash(s):
            n = len(s)
            t = []
            for i in range(1,n):
                a = ord(s[i-1])
                b = ord(s[i])
                if b > a:
                    a+=26
                t.append(a-b)
            return tuple(t)
                

        d = defaultdict(list)
        for x in strings:
            d[hash(x)].append(x)

        return d.values()
        