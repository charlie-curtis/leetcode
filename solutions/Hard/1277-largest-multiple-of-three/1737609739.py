class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:

        ssum = 0
        d = defaultdict(list)
        def high(s1, s2):
            if len(s1) > len(s2):
                return s1
            if len(s2) > len(s1):
                return s2
            return max(s1, s2)
        def greedy(A):
            #print("IN", A)
            d = []
            for li in A.values():
                d+=li
            d.sort(reverse=True)
            res ="".join([str(x) for x in d])
            #print(res)
            if res and res[0] == '0':
                return res[0]
            return res
        for x in digits:
            x = int(x)
            ssum+=x
            d[x%3].append(x)

        for k,v in d.items():
            d[k] = sorted(v, reverse=True)

        if ssum % 3 == 0:
            return greedy(d)
        elif ssum % 3 == 1:
            #either remove 1 1 or 2 2s
            #print("c1")
            can = "" 
            if len(d[1]) >= 1:
                a = d[1].pop()
                can = greedy(d)
                d[1].append(a)
            if len(d[2]) >= 2:
                a = d[2].pop()
                b = d[2].pop()
                can = high(can, greedy(d))
                d[2].append(a)
                d[2].append(b)
            return can
        else:
            #print(d)
            #print("c2")
            #div by 2
            #either remove 2 1s or 1 2
            can = ""
            if len(d[1]) >=2:
                a = d[1].pop()
                b = d[1].pop()
                can = high(can, greedy(d))
                d[1].append(a)
                d[1].append(b)
            if len(d[2]) >=1:
                a = d[2].pop()
                can = high(can, greedy(d))
                d[2].append(a)
            return can