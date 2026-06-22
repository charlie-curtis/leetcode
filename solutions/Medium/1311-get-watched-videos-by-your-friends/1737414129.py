class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

        q = deque()
        q.append(id)

        cur = 0
        seen = set()
        seen.add(id)
        while q:
            last = []
            for i in range(len(q)):
                last.append(q.popleft())
                for f in friends[last[-1]]:
                    if f not in seen:
                        seen.add(f)
                        q.append(f)
            if cur == level:
                break
            cur+=1

        C = Counter()
        for x in last:
            for y in watchedVideos[x]:
                C[y]+=1
        out = []
        for k,v in C.items():
            out.append((v,k))
        out.sort(key = lambda x: (x[0], x[1]))

        return [x[1] for x in out]