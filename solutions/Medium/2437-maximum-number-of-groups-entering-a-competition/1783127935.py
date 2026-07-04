class Solution:
    def maximumGroups(self, grades: List[int]) -> int:

        grades.sort()

        n = len(grades)
        ans = i = 0
        prev = [-1, -1]

        while (i < n):
            ssum = cnt = 0

            while (i < n):
                ssum+=grades[i]
                cnt+=1
                i+=1
                if prev[0] < ssum and prev[1] < cnt:
                    break
            
            if prev[0] < ssum and prev[1] < cnt:
                ans+=1
                prev = [ssum, cnt]
            

        return ans

        