class Item:
    def __init__(self, id, userId, description, dueDate, tags):
        self.id = id
        self.userId = userId
        self.description = description
        self.dueDate = dueDate
        self.tags = set(tags)
    def __hash__(self):
        return self.id
    def __eq__(self, other):
        if isinstance(other,int):
            return self.id == other
        else:
            raise ValueError("Wrong")
class TodoList:

    def __init__(self):
        self.id = 0
        self.d = defaultdict(set)
        

    #needs to return autoincrementID -- not specific to the user
    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        self.id+=1
        print("adding task for user", userId, "with a duedate of", dueDate, "and id of", self.id)
        self.d[userId].add(Item(self.id, userId, taskDescription, dueDate, tags))
        return self.id


    def sortByDueDate(self, items):
        t = [(x.dueDate, x.description) for x in items]
        t.sort()
        return [x[1] for x in t]
        

    #return all tasks that are not marked complete -- ordered by due date
    def getAllTasks(self, userId: int) -> List[str]:
        print("Getting tasks for user", userId)
        return self.sortByDueDate([x for x in self.d[userId]])

    #returns all tasks for the user that have the tag and are not marked complete
    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        print("looking up tasks for user", userId)
        return self.sortByDueDate([x for x in self.d[userId] if tag in x.tags])
        

    #marks a task as complete if it isn't already marked as complete and exists
    def completeTask(self, userId: int, taskId: int) -> None:
        print("attempting to delete task", taskId, "for user", userId)
        print(self.d[userId])
        if taskId in self.d[userId]:
            print("found the task")
            self.d[userId].remove(taskId)
            if taskId in self.d[userId]:
                raise ValueError("Wrong")
        


# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)
