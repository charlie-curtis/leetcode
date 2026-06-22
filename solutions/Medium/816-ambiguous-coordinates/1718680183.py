class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:

        s = s[1:-1]

        ans = set()
        def validate(a):
            if float(a) == 0 and a.find('.') != -1:
                return False
            if a.find('.') != -1 and a[-1] == '0':
                return False
            return True
        def backtrack(i, a, b):
            if i == len(s):
                if validate(a) and validate(b):
                    ans.add((a,b))
                return

            if not b and a and a[-1] != '.':
                #we can start b if there is a and the last char of a isn't .
                backtrack(i+1, a, s[i])
            #we can add a . to b if b exists and a . doesn't already exist
            if b and b.find('.') == -1:
                backtrack(i, a, b + '.')
            #we can extend b if it exists and wouldn't result in double 0
            if b:
                bad = len(b) == 1 and b[0] == '0'
                if not bad:
                    backtrack(i+1, a, b + s[i])

            if not a:
                backtrack(i+1, s[i], None)
            if a and not b and len(s) != i+1:
                bad = len(a) == 1 and a[0] == '0'
                if not bad:
                    backtrack(i+1, a + s[i], None)
                if a and a.find('.') == -1:
                    backtrack(i, a + '.', None)
            #we can either add a decimal (If there isn't already a decimal and it isn't an extraneous 0)
            #or start a new number (if we haven't already)
            
               
        backtrack(0, None, None)
        return ['(' + a + ', ' + b + ")" for a,b in ans]