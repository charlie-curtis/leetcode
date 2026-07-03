class Solution:
    def sumOfThree(self, n: int) -> List[int]:

        if n % 3 == 0:
            v = n//3
            return [v-1,v,v+1]
        return []
        