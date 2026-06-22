class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        #math intuition - #editorial - flunked

        #easy in hindsight, lol (it always is)


        seen = set()
        l = 1
        n = 1
        while n%k != 0:
            if n in seen:
                return -1
            seen.add(n)
            n*=10
            n+=1
            l+=1
            n%=k
        
        return l