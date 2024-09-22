class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        go = lambda x: "FizzBuzz" if x % 15 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else str(x)

        return [go(x) for x in range(1,n+1)]
        