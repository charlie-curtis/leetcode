class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:


        target = coordinates[k]

        lowers = [x for x in coordinates if x[0] < target[0] and x[1] < target[1]]
        uppers = [x for x in coordinates if x[0] > target[0] and x[1] > target[1]]

        def lis(A):
            A.sort(key=lambda x: (x[0], -x[1]))

            li = []
            for _,x in A:
                idx =bisect_left(li,x)
                if idx == len(li):
                    li.append(x)
                else:
                    li[idx] = x
            return len(li)


        return lis(lowers) + lis(uppers) + 1