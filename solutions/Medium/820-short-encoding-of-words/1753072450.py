class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:

        A = [[-len(word), word] for word in words]

        out = []
        A.sort()
        for _,s in A:
            found = False
            for t in out:
                res = t.rfind(s)
                if res != -1 and res+len(s)==len(t):
                    found = True
                    break
            if not found:
                out.append(s)

        S = '#'.join([t for t in out])
        print(S)
        return len(S) + 1
        

        