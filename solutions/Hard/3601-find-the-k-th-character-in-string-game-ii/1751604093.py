class Solution:
    def kthCharacter(self, k: int, ops: List[int]) -> str:


        #1. Get power of 2 gte k

        P = 1
        while P < k:
            P*=2

        #2. while P > 0, determine whether the value of K appears in the left or right hand side of the formed string

        SIDES = []
        #so if k = 5, P = 8, then we have 1-4, 5-8 as the sides
        while P > 0:

            half = P//2
            if k > half:
                print("RIGHT")
                SIDES.append(1)
                k-=half
            else:
                print("LEFT")
                SIDES.append(0)
            P = half
        

        SIDES.pop()
        SIDES = SIDES[::-1]
        ans = 0
        for i,x in enumerate(SIDES):
            if x == 1 and ops[i] == 1:
                ans+=1
        return chr(ord('a') + (ans%26))
