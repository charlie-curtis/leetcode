class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        p1 = ""
        mapp = ""

        i = 0
        #for convenience, I'm formatting the "*" character specifically. for a string "a*b", it will make the string "*b" with a mapping of the first '*' to its preceeding char, 'a'
        while i < len(p):
            if i+1 < len(p) and p[i+1] == '*':
                p1+='*'
                mapp+=p[i]
                i+=2
            else:
                p1+=p[i]
                mapp+=p[i]
                i+=1
        p = p1
        m = len(s)
        n = len(p)
        @cache
        def check(i,j):
            if i == m or j == n:
                #if we exhausted either the string or the pattern, check if we're good.
                #we're good if we exhausted both at the same time or the only thing remaining are optional '*' characters
                return i == m and (j == n or set(p[j:n]) == set('*'))
            
            if p[j] == '.' or s[i] == p[j]:
                #no special characters, must be a 1-1 match (with special handling of '.')
                return check(i+1,j+1)
            
            if p[j] != '*':
                return False
            
            #simulate 0 match
            if check(i, j+1): return True

            if s[i] != mapp[j] and mapp[j] != '.': return False
            #simulate 1+ match
            if check(i+1,j): return True
            #simulate exactly 1 match
            if check(i+1,j+1):return True

            return False

            
        return check(0,0)