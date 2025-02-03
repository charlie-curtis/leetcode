class Solution:
    def unhappyFriends(self, n: int, pref: List[List[int]], pairs: List[List[int]]) -> int:

        n = len(pref)

        p = {}
        for u,v in pairs:
            p[u] = v 
            p[v] = u
        

        unhappy = set()
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                partner1 = p[i]
                partner2= p[j]
                p1 = pref[i].index(partner1)
                p2 = pref[j].index(partner2)

                p3 = pref[i].index(j)
                p4 = pref[j].index(i)

                if p3 < p1 and p4 < p2:
                    unhappy.add(i)
                    unhappy.add(j)
        return len(unhappy)
