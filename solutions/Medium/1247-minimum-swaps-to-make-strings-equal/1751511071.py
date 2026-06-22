class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:


        #xyxy, xxxx
        
        #_y_y, _x_x


        #this is a case work problem
        #case 1: the number of x's aren't even (meaning the # of y's also can't be even) -> no solution exists
        #next, cancel out any string positions that already match

        #case 2: greedily use operation 2 (which is where you pair 'xx' with 'yy'). In that case, you can use 1 move to turn it into 'xy'
        #case 3: whatever is remaining has to be 'xy' 'xy' which is 2 moves
        s1x = s1.count('x')
        s1y = s1.count('y')
        s2x = s2.count('x')
        s2y = s2.count('y')

        if (s1x + s2x) % 2 != 0:
            return -1
        
        n = len(s1)
        for i in range(n):
            if s1[i] == s2[i]:
                if s1[i] == 'x':
                    s1x-=1
                    s2x-=1
                else:
                    s1y-=1
                    s2y-=1
        
        ans = 0
        #at this point, the remaining counts are mismatched
        a = min(s1x, s2y)//2
        b = min(s1y, s2x)//2
        s1x-=a*2
        s2y-=a*2
        s1y-=b*2
        s2x-=b*2

        print(s1x, s1y)

        ans+=a
        ans+=b
        ans+=s1x + s1y
        return ans
        