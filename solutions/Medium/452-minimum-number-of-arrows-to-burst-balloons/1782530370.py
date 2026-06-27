class Solution:
    def findMinArrowShots(self, pts: List[List[int]]) -> int:
        pts.sort(key=lambda x: x[1])

        far = pts[0][1]
        ans = 1
        for start,end in pts:
            if far < start:
                far = end
                ans+=1
        return ans
        