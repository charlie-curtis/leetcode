class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], dirs: str) -> List[int]:
        stack = []

        A = list(zip(positions, healths,dirs, [i for i in range(len(healths))]))
        A.sort()

        for pos, health, dir, idx in A:
            if dir == 'R':
                stack.append([pos,health,dir, idx])
                continue
            
            died = False
            while stack and stack[-1][2] == 'R' and stack[-1][1] and not died:
                t = stack.pop()
                if health == t[1]:
                    health = 0
                    died = True
                elif t[1] > health:
                    health = 0
                    t[1]-=1
                    stack.append(t)
                    died = True
                else:
                    died = False
                    health-=1
            if not died:
                stack.append([pos,health,dir, idx])

        
        stack.sort(key= lambda x: x[3])
        return [x[1] for x in stack]
            

        