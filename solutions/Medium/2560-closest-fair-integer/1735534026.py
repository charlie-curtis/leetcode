class Solution:
    def closestFair(self, n: int) -> int:
        
        #odd length strings
        l = len(str(n))
        if l % 2:
            l+=1
            return int('1'+ '0'*(l//2) + '1'*(l//2-1))

        
        #even length strings

        def find(s, b, upped):
            if not s:
                return "" if b == 0 else -1
            
            d = int(s[0])
            if upped:
                #if we previously increased a prev number, we can use the whole range
                d = 0
            for x in range(d,10):
                t = b + (1 if x % 2 == 0 else -1)
                res = find(s[1:], t, upped or x > d)
                if res != -1:
                    return str(x) + res

            return -1

        res = find(str(n), 0, False)
        if res == -1:
            #if we couldn't find anything with this current set of numbers
            #(so like 9999), then multiply by 10 and call the original function to get
            #100011
            return self.closestFair(n*10)
        return int(res)
            

        #1109
        #balance = -2