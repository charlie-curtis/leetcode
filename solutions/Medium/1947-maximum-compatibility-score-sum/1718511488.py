class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:


        def compute(i,j):
            return sum([len(set(x)) == 1 for x in zip(students[i], mentors[j])])

        def backtrack(i, mentors_used):

            if i == len(students):
                return 0

            best = 0
            for j in range(len(mentors)):
                if mentors_used&(1<<j) > 0:
                    continue
                candidate = compute(i,j) + backtrack(i+1, mentors_used|(1<<j))
                best = max(best, candidate)

            return best

        return backtrack(0, 0)