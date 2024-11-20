class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:



        #abcd (3,3) i, j
        #bccda (4,4) a,b

        s1 = [x for x in firstString]
        s2 = [x for x in secondString]

        d1 = {}
        d2 = {}
        for i in range(len(s1)-1, -1, -1):
            d1[s1[i]] = i

        for i in range(len(s2)):
            d2[s2[i]] = i


        d = defaultdict(int)
        for i in range(26):
            letter = chr(ord('a') + i)
            if letter not in d1 or letter not in d2:
                continue
            
            diff = d1[letter] - d2[letter]
            d[diff]+=1

        if len(d) == 0:
            return 0
        small = min(d.keys())
        return d[small]