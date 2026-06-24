class Solution:
    def simplifyPath(self, path: str) -> str:

        X = path.split("/")

        out = deque()

        for x in X:
            if x == '' or x == '.':
                continue
            elif x == '..':
                if len(out):
                    out.pop()
            else:
                out.append(x)
        
        if not out:
            return '/'
        return '/' + '/'.join(out)
        