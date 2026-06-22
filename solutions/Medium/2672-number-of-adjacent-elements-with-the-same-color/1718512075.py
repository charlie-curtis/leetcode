class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]*len(queries)

        A = [0]*n
        ans = []
        pairs = 0

        for index,color in queries:
            prev_left = None if index == 0 else A[index-1]
            prev_right = None if index == len(A)-1 else A[index+1]
            cur = A[index]
            if prev_left == cur and cur !=0:
                pairs-=1
            if prev_right == cur and cur !=0:
                pairs-=1
            A[index] = color
            if prev_left == color:
                pairs+=1
            if prev_right == color:
                pairs+=1
            ans.append(pairs)
        return ans 
        