class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:


        row_count = Counter()
        col_count = Counter()
        n = len(rooks)

        for r,c in rooks:
            row_count[r]+=1
            col_count[c]+=1


        j = 0
        ans = 0
        for i in range(n):
            if row_count[i] == 0:
                #need to borrow
                while row_count[j] <= 1:
                    j+=1
                ans+=abs(i-j)
                row_count[j]-=1
                row_count[i]+=1

        j = 0
        for i in range(n):
            if col_count[i] == 0:
                #need to borrow
                while col_count[j] <= 1:
                    j+=1
                ans+=abs(i-j)
                col_count[j]-=1
                col_count[i]+=1

        return ans


        