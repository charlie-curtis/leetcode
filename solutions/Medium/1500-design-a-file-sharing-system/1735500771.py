class FileSharing:

    def __init__(self, m: int):
        self.available = [x for x in range(1,m+1)]
        heapify(self.available)
        self.chunks = defaultdict(SortedSet)
        self.d = defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        id = heapq.heappop(self.available)
        self.d[id] = set(ownedChunks)
        for x in ownedChunks:
            self.chunks[x].add(id)
        return id
        

    def leave(self, userID: int) -> None:
        heapq.heappush(self.available, userID)
        chunks = self.d[userID]
        for x in chunks:
            self.chunks[x].remove(userID)
        self.d[userID] = set()
        

    def request(self, userID: int, chunkID: int) -> List[int]:
        users = self.chunks[chunkID]
        res = list(users)
        if len(users) != 0:
            self.d[userID].add(chunkID)
            self.chunks[chunkID].add(userID)
        return res


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)