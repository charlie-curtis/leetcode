class Solution:
    def originalDigits(self, s: str) -> str:


        #zero -> 'z'
        #two -> 'w'
        #four -> 'u'
        #six -> 'x'
        #eight -> 'g'
        #three -> 'h'
        #five -> 'f'
        #one -> 'o'
        #seven 'v'
        #nine 'e'


        cnts = [0]*10
        C = Counter(s)
        DAG = [
            ['z', 'zero', 0],
            ['w', 'two', 2],
            ['u', 'four', 4],
            ['x', 'six', 6],
            ['g', 'eight', 8],
            ['h', 'three', 3],
            ['f', 'five', 5],
            ['o', 'one', 1],
            ['v', 'seven', 7],
            ['e', 'nine', 9]
        ]

        for letter, s, pos in DAG:
            cnt = C[letter]
            cnts[pos]+=cnt
            for x in s:
                C[x]-=cnt
        
        out = ""
        for i,x in enumerate(cnts):
            if x > 0:
                out+=(str(i)*x)
        return out