class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        blocked = defaultdict(list)
        for row, seat in reservedSeats:
            blocked[row].append(seat)

        impacted = len(blocked)

        ans = 0
        for li in sorted(blocked.values()):
            middle = all([x not in li for x in [4,5,6,7]])
            left = all([x not in li for x in [2,3,4,5]])
            right = all([x not in li for x in [6,7,8,9]])

            if left and right:
                ans+=2
            elif any([middle,left,right]):
                ans+=1

        return 2*(n -impacted)+ans