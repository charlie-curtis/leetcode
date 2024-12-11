class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:

        d = defaultdict(int)

        n = len(s)

        for i in range(len(words)):
            word = words[i]
            m = len(word)
            for j in range(n-m+1):
                if word == s[j:j+m]:
                    d[j]+=1
                    d[j+m]-=1

        cur = 0
        isOpen = False
        out = []
        for i,x in enumerate(s):
            cur+=d[i]
            if not isOpen and cur > 0:
                out.append("<b>")
                isOpen = True
            elif isOpen and cur == 0:
                out.append("</b>")
                isOpen = False
            out.append(x)

        if isOpen:
            out.append("</b>")
        
        return "".join(out)

            
            

