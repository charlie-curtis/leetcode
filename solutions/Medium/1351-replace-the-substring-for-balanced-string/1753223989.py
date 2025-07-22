class Solution:
    def balancedString(self, s: str) -> int:

        C = Counter(s)
        E = C['E']
        W = C['W']
        R = C['R']
        Q = C['Q']

        if E == W == R == Q:
            return 0

        E1 = W1 = R1 = Q1 = 0
        j = 0
        n = len(s)
        ans = n
        target = len(s)//4
        for i,x in enumerate(s):
            if x == 'E':
                E1+=1
            elif x == 'W':
                W1+=1
            elif x == 'R':
                R1+=1
            else:
                Q1+=1
            
            E2 = E - E1
            W2 = W - W1
            R2 = R - R1
            Q2 = Q - Q1

            #if the max character outside this window is <= target,
            #that means we can balance the string by only adjusting chars
            #that are INSIDE this window
            while j<= i and max(E2,W2,R2,Q2) <= target:
                ans = min(ans, i-j+1)

                if s[j] == 'E':
                    E1-=1
                elif s[j] == 'W':
                    W1-=1
                elif s[j] == 'R':
                    R1-=1
                else:
                    Q1-=1
                j+=1

                E2 = E - E1
                W2 = W - W1
                R2 = R - R1
                Q2 = Q - Q1
        return ans