class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.pq = []
        self.d = {}
        for userId, taskId, priorityId in tasks:
            self.pq.append([-priorityId, -taskId, userId])
            self.d[taskId] = [priorityId, userId]
        heapq.heapify(self.pq)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:

        self.d[taskId] = [priority, userId]
        heappush(self.pq, [-priority, -taskId, userId])


    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.d[taskId][1]
        old = self.d[taskId][0]
        if old == newPriority:
            return
        self.d[taskId] = [newPriority, userId]
        heappush(self.pq, [-newPriority, -taskId, userId])
        

    def rmv(self, taskId: int) -> None:
        del self.d[taskId]

    def execTop(self) -> int:
        while self.pq:
            top = heapq.heappop(self.pq)
            p = -top[0]
            taskId = -top[1]
            u = top[2]



            if taskId in self.d and self.d[taskId] == [p,u]:
                self.rmv(taskId)
                return u

        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()