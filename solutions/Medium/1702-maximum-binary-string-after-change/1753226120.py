class Solution:
    def maximumBinaryString(self, s: str) -> str:

        #00 -> 10
        #10 -> 01


        #010 -> 001 -> 101
        #001111 -> you can bring a 0 over if there is 1 to the right

        #process from L to R. Greedy
        #cases
        #00 -> turn to 10 and recurse with i+1, i+2
        #10 -> recurse with i+1, i+2
        #01 -> we want to swap the 0 and 1, but how? need to look to the right to find a '00' to swap it with
        #11 -> recurse with i+1, i+2
        out = []
        n = len(s)
        s = [x for x in s]
        j = 0
        for i in range(n-1):
            c = ''.join(s[i:i+2])
            if c in ['00', '10', '11']:
                #we are able to set the leading char to 1 without any further changes
                out.append(1)
            elif c == '01':
                j = max(j, i+2)
                while j < n and s[j] != '0':
                    j+=1
                if j < n:
                    s[j] = '1'
                    s[i+1] = '0'
                    out.append(1)
                else:
                    out.append(0)
            else:
                raise ValueError("Wrong")
        out.append(int(s[-1]))
        
        return ''.join([str(x) for x in out])