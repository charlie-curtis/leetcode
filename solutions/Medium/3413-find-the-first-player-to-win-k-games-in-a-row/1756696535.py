class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:

        pos = {}
        for i,x in enumerate(skills):
            pos[x] = i

        streak = 0
        mx = max(skills)
        skills = deque(skills)

        last = -1
        while skills:
            first,second = skills.popleft(), skills.popleft()
            winner = max(first,second)
            if winner == last:
                streak+=1
            else:
                streak = 1
                last = winner

            if streak == k or winner == mx:
                return pos[winner]
            skills.appendleft(winner)