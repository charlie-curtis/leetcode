class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        #idea: simulate trying every language and see which one produces the best score.
        #if a common language already exists for a friendship, just filter that friendship out
        languages = [set(l) for l in languages]
        friendships = [[u-1,v-1] for (u,v) in friendships if len(languages[u-1] & languages[v-1]) == 0]

        out = 10**9
        for t in range(1, n+1):
            can = set()
            for u,v in friendships:
                l1,l2 = languages[u], languages[v]
                if t not in l1:
                    can.add(u)
                if t not in l2:
                    can.add(v)
            out = min(len(can),out)
        return out
        