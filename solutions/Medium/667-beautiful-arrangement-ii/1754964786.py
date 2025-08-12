class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:

        #say k = 3, n = 10

        #we need to generate the differences 3,2,1
        #we need our biggest k to start from 1


        #k = 5, n = 10
        #5,4,3,2,1

        #1, 6, 2, 5, 3, 4 (what about 7-10?) pad to end? Yes, since we started with 1 and 6, we know that any number we pad to the end will be not introduce a new k value
        #1,6,2,5,3,4,7,8,9,10

        out = [1]
        j = high = 0
        for i in range(k, 0, -1):
            if j % 2 == 0:
                out.append(out[-1]+i)
            else:
                out.append(out[-1]-i)
            j+=1
        
        for i in range(k+2, n+1):
            out.append(i)
        return out