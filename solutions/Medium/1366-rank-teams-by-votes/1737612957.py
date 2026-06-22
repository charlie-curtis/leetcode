class Solution:
    def rankTeams(self, votes: List[str]) -> str:

        n = len(votes[0])

        d = {}
        for s in votes:
            for i in range(len(s)):
                c = s[i]
                if c not in d:
                    d[c] = [0]*n
                d[c][i]+=1


        A = []
        for x in d.keys():
            A.append([tuple(d[x]), -ord(x)])

        A.sort(reverse=True)
        return ''.join([chr(abs(x[1])) for x in A])