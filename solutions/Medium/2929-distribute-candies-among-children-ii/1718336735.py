class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:



        first_person_min = max(0, n - 2*limit)
        first_person_max = min(n, limit)

        ans = 0
        for i in range(first_person_min, first_person_max + 1):
            second_person_min = max(0, n-i - limit)
            second_person_max = min(limit, n-i)
            ans+= 1 + second_person_max - second_person_min
        return ans