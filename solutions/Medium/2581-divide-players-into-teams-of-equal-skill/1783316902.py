class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        prev = -1
        n = len(skill)
        ans = 0
        for i in range(n):
            if i > n-1-i:
                break
            t = skill[i] + skill[n-1-i]
            if prev != -1 and prev != t:
                return -1
            prev = t
            ans+=skill[i]*skill[n-1-i]
        return ans
            
        