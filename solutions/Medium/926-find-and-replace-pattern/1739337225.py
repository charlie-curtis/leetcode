class Solution:
    def findAndReplacePattern(self, words: List[str], p: str) -> List[str]:
        def check(s):
            d={}
            rd={}
            for a,b in zip(s,p):
                f1= a in d
                f2 = b in rd
                if f1 != f2: return False
                if f1:
                    if d[a] != b or rd[b] != a: return False
                d[a] = b
                rd[b] = a
            return True
        
        return [x for x in words if check(x)]
        