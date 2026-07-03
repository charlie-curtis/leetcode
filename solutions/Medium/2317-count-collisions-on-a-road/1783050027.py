class Solution:
    def countCollisions(self, dirs: str) -> int:


        stack = []
        ans = 0
        for x in dirs:
            if x == 'L' and stack and stack[-1] in 'RS':
                if stack.pop() == 'R':
                    ans+=2
                else:
                    ans+=1
                while stack and stack[-1] == 'R':
                    #after the collision, any cars that were traveling right will pile up
                    stack.pop()
                    ans+=1
                #car won't be moving
                stack.append('S')
            elif x == 'S' and stack and stack[-1] == 'R':
                while stack and stack[-1] == 'R':
                    stack.pop()
                    ans+=1
                stack.append('S')
            elif x != 'L':
                stack.append(x)
        return ans