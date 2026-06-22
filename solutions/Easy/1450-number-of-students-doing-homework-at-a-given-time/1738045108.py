class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        A = list(zip(startTime, endTime))


        ans = 0
        for a,b in A:
            if a<=queryTime<=b:
                ans+=1
        return ans
            
        