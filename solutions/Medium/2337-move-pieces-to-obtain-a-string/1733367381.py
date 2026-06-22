class Solution:
    def canChange(self, start: str, target: str) -> bool:

        lefts = deque()
        rights = deque()
        blanks = deque()

        for i,x in enumerate(start):
            if x == 'L':
                lefts.append(i)
            elif x == 'R':
                rights.append(i)
            else:
                blanks.append(i)

        
        for x in target:
            if x == 'L':
                if not lefts:
                    return False
                l = lefts.popleft()
                #if we need a left, we can grab it as long as it isn't blocked by a R. This simulates sliding it over to the left
                nxt_right = rights[0] if rights else 1e10
                if min(nxt_right, l) != l:
                    return False
            elif x == 'R':
                if not rights:
                    return False
                r = rights.popleft()
                nxt_left = lefts[0] if lefts else 1e10
                nxt_blank = blanks[0] if blanks else 1e10
                if min(nxt_left, nxt_blank, r) != r:
                    return False
            else:
                #we need a blank, and we can get it as long as there isn't an L blocking it
                if not blanks:
                    return False
                b = blanks.popleft()
                nxt_left = lefts[0] if lefts else 1e10
                if min(nxt_left, b) != b:
                    return False
        if len(blanks) + len(rights) + len(lefts) != 0:
            raise ValueError("Wrong")
        return True


        