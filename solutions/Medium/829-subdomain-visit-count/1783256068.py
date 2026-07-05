class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        C = Counter()
        for l in cpdomains:
            cnt, dom = l.split(" ")
            prev=""
            for sub in dom.split(".")[::-1]:
                x=sub
                if prev:
                    x=sub + "." + prev
                prev=x
                C[x]+=int(cnt)
        return [str(cnt) + " " + sub for sub,cnt in C.items()]