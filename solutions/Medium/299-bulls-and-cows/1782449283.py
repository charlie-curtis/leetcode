class Solution:
    def getHint(self, secret: str, guess: str) -> str:


        C = Counter(secret)
        C2 = Counter(guess)

        a = sum([1 if a==b else 0 for (a,b) in zip(secret,guess)])

        b = sum([min(C[x], C2[x]) for x in C.keys()]) - a

        return str(a) + "A" + str(b) + "B"


        