class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

        def f(x):
            if x <= startValue:
                return startValue-x
            if x%2:
                return 1 + f(x+1)
            return 1 + f(x//2)

        return f(target)