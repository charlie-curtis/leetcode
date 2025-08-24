class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:

        stack = []
        for x in A:
            if x > 0:
                stack.append(x)
                continue
            dead = False
            while stack and stack[-1] > 0:
                if abs(stack[-1]) > abs(x):
                    dead = True
                    break
                elif abs(stack[-1]) < abs(x):
                    stack.pop()
                else:
                    stack.pop()
                    dead = True
                    break
            if not dead:
                stack.append(x)
        return stack



        