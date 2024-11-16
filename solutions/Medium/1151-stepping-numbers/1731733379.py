class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:



        sset = set()
        def bt(stack):

            if stack:
                intval = int(''.join([str(x) for x in stack]))
                if intval > high:
                    return
                if low <= intval <= high:
                    sset.add(intval)

            if not stack:
                stack = []
                for i in range(0,10):
                    stack.append(i)
                    bt(stack)
                    stack.pop()
            else:
                last = stack[-1]
                for x in [last-1, last+1]:
                    if 0 <= x < 10:
                        stack.append(x)
                        bt(stack)
                        stack.pop()

        bt([])
        return sorted(sset)

        