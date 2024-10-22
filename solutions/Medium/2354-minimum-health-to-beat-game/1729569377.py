class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:

        mmax = max(damage)
        n = len(damage)
        for i in range(n):
            if damage[i] == mmax:
                damage[i] = max(0, damage[i]-armor)
                break
        
        return sum(damage)+1
        '''
        has = ans = borrowed = 0
        for x in damage:
            if has <= x:
                borrowed = x-has+1
                has+=borrowed
                ans+=borrowed
            has-=x
        return ans 
        '''

        