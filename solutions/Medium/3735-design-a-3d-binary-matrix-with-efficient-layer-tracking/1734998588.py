class Matrix3D:

    def __init__(self, n: int):
        self.n = n
        self.pq = []
        self.d = defaultdict(set)
        

    def setCell(self, x: int, y: int, z: int) -> None:
        self.d[x].add((y,z))
        l = len(self.d[x])
        heapq.heappush(self.pq, (-l, -x))
        

    def unsetCell(self, x: int, y: int, z: int) -> None:
        self.d[x].discard((y,z))
        

    def largestMatrix(self) -> int:
        while self.pq:
            v, x = -self.pq[0][0], -self.pq[0][1]
            if v == len(self.d[x]):
                break
            heapq.heappop(self.pq)

        if not self.pq:
            return self.n-1
        return -self.pq[0][1]
        


# Your Matrix3D object will be instantiated and called as such:
# obj = Matrix3D(n)
# obj.setCell(x,y,z)
# obj.unsetCell(x,y,z)
# param_3 = obj.largestMatrix()