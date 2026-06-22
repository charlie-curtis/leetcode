class Solution:
    def reorderSpaces(self, text: str) -> str:

        t = text.split(" ")
        n = len(t)
        out = [x for x in t if x != '']
        space = text.count(' ')
        if len(out) == 1:
            print("hit")
            return ''.join(out) + ' '*space
        print("there are", space, "spaces")
        m = space//(len(out)-1)
        print("m is", m, "because n-1=", n-1)
        rem = space - m*(len(out)-1)

        ans = ""
        for i,x in enumerate(out):
            ans+=x
            if i != len(out)-1:
                ans+=' ' * m
            else:
                ans+=' ' * rem
        return ans
        
        