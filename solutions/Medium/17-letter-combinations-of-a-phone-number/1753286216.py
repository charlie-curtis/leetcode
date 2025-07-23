class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        d = {
            2 : 'abc',
            3 : 'def',
            4 : 'ghi',
            5 : 'jkl',
            6 : 'mno',
            7 : 'pqrs',
            8 : 'tuv',
            9 : 'wxyz'
        }


        n = len(digits)
        if n == 0:
            return []
        out = []
        def bt(i, cur):
            if i == n:
                out.append(''.join(cur))
                return
            for nxt in d[int(digits[i])]:
                cur.append(nxt)
                bt(i+1, cur)
                cur.pop()
            

        bt(0, [])
        return out
        