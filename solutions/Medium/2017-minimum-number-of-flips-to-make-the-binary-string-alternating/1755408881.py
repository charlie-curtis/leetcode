class Solution:
    def minFlips(self, s: str) -> int:

        n = len(s)
        evens = [0,0]
        odds = [0,0]

        for i,x in enumerate(s):
            x = int(x)
            if i%2:
                odds[x%2]+=1
            else:
                evens[x%2]+=1
        
        if n % 2 == 0:
            #if the size of the array is even, we can't ever change the grouping of numbers
            #by rotating the front
            #example [a,b,c,d] -> (a,c) and (b,d) will always be grouped together, so just figure out whether it's optimal to start the sequence with 10 or 01.
            return n - max(evens[0] + odds[1], evens[1] + odds[0])

        best = 10**9

        #if the array length is odd, we can change the grouping
        #[a,b,c] -> a,c is originally grouped. After rotating, [b,c,a] -> now b,a is groupkd
        for i in range(n):
            best = min(best, n - max(evens[0] + odds[1], evens[1] + odds[0]))
            x = int(s[i])
            #assume 'i' is the head right before we rotate it, so it'll always be an even idx
            evens[x%2]-=1
            odds[x%2]+=1
            evens,odds = odds,evens
        
        return best