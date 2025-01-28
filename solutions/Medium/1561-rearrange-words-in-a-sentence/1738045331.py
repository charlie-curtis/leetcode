class Solution:
    def arrangeWords(self, text: str) -> str:

        A = []
        for i,x in enumerate(text.split()):
            A.append([len(x), i, x.lower()])

        A.sort()

        res = " ".join([a[2] for a in A])
        return res[0].upper() + res[1:]
        