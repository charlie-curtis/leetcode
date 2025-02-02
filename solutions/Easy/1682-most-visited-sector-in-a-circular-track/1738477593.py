class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        A = list(zip(rounds, rounds[1:]))

        C = Counter()
        for i,(s,e) in enumerate(A):
            s-=1
            e-=1

            if i != 0:
                C[s]-=1
            while s != e:
                C[s]+=1
                s+=1
                s%=n
            C[e]+=1



        mmax = max(C.values())
        out = []
        for k in sorted(C.keys()):
            if C[k] == mmax:
                out.append(k+1)
        return out
        