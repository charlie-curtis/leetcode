# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        d = {
            'U': ['U', 'R', 'D', 'L'],
            'D': ['D', 'L', 'U', 'R'],
            'R': ['R', 'D', 'L', 'U'],
            'L': ['L', 'U', 'R', 'D']
        }

        def switch(cur, desired):
            mmap = d[cur]
            idx = mmap.index(desired)
            if idx < 2:
                for _ in range(idx):
                    robot.turnRight()
            else:
                idx = 4 -idx
                for _ in range(idx):
                    robot.turnLeft()

        i = j = 0
        seen = set()
        def dfs(i,j, dir):
            if (i,j) in seen:
                return
            seen.add((i,j))
            robot.clean()

            
            if (i+1, j) not in seen:
                #go down
                switch(dir, 'D')
                didMove = robot.move()
                if didMove:
                    dfs(i+1, j, 'D')
                switch('D', 'U')
                if didMove:
                    res = robot.move()
                    if not res:
                        raise ValueError("Wrong")
                switch('U', dir)
            
            
            if (i-1, j) not in seen:
                #go up
                switch(dir, 'U')
                didMove = robot.move()
                if didMove:
                    dfs(i-1, j, 'U')
                switch('U', 'D')
                if didMove:
                    res = robot.move()
                    if not res:
                        raise ValueError("Wrong")
                switch('D', dir)
            
            if (i, j-1) not in seen:
                #go left
                switch(dir, 'L')
                didMove = robot.move()
                if didMove:
                    dfs(i, j-1, 'L')
                switch('L', 'R')
                if didMove:
                    res = robot.move()
                    if not res:
                        raise ValueError("Wrong")
                switch('R', dir)

            if (i, j+1) not in seen:
                #go right
                switch(dir, 'R')
                didMove = robot.move()
                if didMove:
                    dfs(i, j+1, 'R')
                switch('R', 'L')
                if didMove:
                    res = robot.move()
                    if not res:
                        raise ValueError("Wrong")
                switch('L', dir)

        dfs(0,0,'U')


            

        