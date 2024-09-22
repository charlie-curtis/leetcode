class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)

        def rev(l, r):
            while l <= r:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1

        rev(0, n-1) #reverse the entire string
        spaces = [-1]
        for i,x in enumerate(s):
            #index the spaces
            if x == " ":
                spaces.append(i)
        spaces.append(n)
        
        for i in range(1,len(spaces)):
            #reverse every word between the spaces
            prev_space = spaces[i-1]
            cur_space = spaces[i] 
            rev(prev_space+1, cur_space-1)


        