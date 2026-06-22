class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        out=[]
        n=len(s)

        def bt(cur):
            if len(cur)==n:
                out.append(cur)
                return
            i = len(cur)
            if s[i].isalpha():
                bt(cur+s[i].lower())
                bt(cur+s[i].upper())
            else:
                bt(cur+s[i])
        bt("")
        return out
                
        