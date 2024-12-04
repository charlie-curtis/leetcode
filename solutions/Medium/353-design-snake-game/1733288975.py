class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width, self.height = width, height
        pos = (0,0)
        self.state = deque([pos])
        self.hash = Counter([pos])
        self.food = deque(food)
        self.d_map = {
            'U': [-1, 0],
            'D': [1, 0],
            'L': [0, -1],
            'R': [0, 1]
        }

    def isDead(self) -> bool:
        x, y = self.state[0]
        h,w = self.height, self.width
        return x < 0 or y < 0 or x == h or y == w or self.hash[(x,y)] > 1

    def moveInDirection(self, d) -> None:
        d_map = self.d_map

        #add head based on dir
        x,y = self.state[0]
        x+=d_map[d][0]
        y+=d_map[d][1]
        self.state.appendleft((x,y))
        self.hash[(x,y)]+=1

        if not self.food or self.food[0] != [x,y]:
            #remove the last length
            i,j = self.state.pop()
            self.hash[(i,j)]-=1
            if self.hash[(i,j)] < 0:
                raise ValueError("Wrong")
        else:
            #we ate this food
            self.food.popleft()


    def getScore(self) -> int:
        return -1 if self.isDead() else len(self.state)-1

    def move(self, direction: str) -> int:

        self.moveInDirection(direction)
        return self.getScore()
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)