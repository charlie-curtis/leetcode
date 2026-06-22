class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)

        books = books[::-1]
#        print(books)
        nxt = [n]*n
        stack = []

        for i in range(n-1,-1,-1):
            #print(i, stack)
            while stack and books[stack[-1]] + stack[-1]-i >= books[i]:
                stack.pop()
            
            if stack:
                #print("sanity", i)
                #print(stack[-1], books[stack[-1]], i-stack[-1], books[i])
                nxt[i] = stack[-1]
            stack.append(i)


        #print(nxt)
        pref = list(accumulate(books, initial=0))

        #i = 0, nxt = 1
        #say i = 3... we want to sum from 0 to i = 2 inclusive,
        @cache
        def dp(i):
            if i == n:
                return 0

            #8 7 # 6
            rem = dp(nxt[i])
            window = nxt[i]-i
            l = books[i]
            r = max(books[i] - window, 0)
            
            btwn = l*(l+1)//2 - r*(r+1)//2
#            print("I'm ", books[i], "and my btwn is", btwn, "and the rem is", rem)
            return rem + btwn


        #print([dp(i) for i in range(n)])
        return max([dp(i) for i in range(n)])


            #  1 2 3
            #0 1 3 6
        