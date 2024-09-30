class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:


        A, B = nums1, nums2
        dpA = [1]*len(A)
        dpB = [1]*len(B)

        for i in range(1,len(A)):
            a_options = [1]
            if A[i] >= A[i-1]:
                a_options.append(dpA[i-1]+1)
            if A[i] >= B[i-1]:
                a_options.append(dpB[i-1]+1)

            b_options = [1]
            if B[i] >= B[i-1]:
                b_options.append(dpB[i-1]+1)
            if B[i] >= A[i-1]:
                b_options.append(dpA[i-1]+1)

            dpA[i] = max(a_options)
            dpB[i] = max(b_options)

        return max(max(dpA), max(dpB))
            

        #7 ,8, 9, 1,2,3,4,5,6,7,8,9...
        #10,11,10,11,2,12,13,4

        #4, 8, 1
        #9  9  7

        #4,8
        #1,7

        #1,9,10

        #A if both are greater than li[-1], append the smaller
        #B if one is greater and one isn't, append and insert
        #C if both are smaller, insert both?

        li = []
        for x,y in A:
            x,y = max(x,y), min(x,y)
            idxY = bisect_right(li, y)
            idxX = bisect_right(li, x)

            if idxY == len(li): #A
                li.append(y)
                print(li)
                continue
            elif idxX == len(li): #B
                li.append(x)
                li[idxY] = y
            else:
                li[idxX] = x
                li[idxY] = y
            print(li)
        print(li)
        return len(li)

        #[4,2]
        #10,4

        #3 7 18, 19, 1,2,3,0,1,2
        #x x x   0   20 21 22 23

        3,7,19,19,20,21,22
        1,2,3,22,23
        0,1,2