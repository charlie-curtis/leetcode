class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:

        #3,1,7,2,5
        #[3],[1],[7],[2],[5] = 7
        #[3,1],[1,7], [7,2],[2,5] = 2
        #[3,1,7], [1,7,2], [7,2,5] = 2
        #[3,1,7,2], [1,7,2,5] = 1
        #[3,1,7,2,5] = 1


        #next smaller number to each side

        #3,5,2,7,8,3,2
    #      ^     ^
        #so 7 will never be considered until the sizes get to 2 (e.g. [7,8])
        #basically for each number, find the next closest lower number to the left and right. if either
        #of those numbers are k away, then it's eligible for that k+1 window

        #monotonic stack

        n = len(nums)
        to_left = [-1]*n
        to_right = [n]*n

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                to_left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                to_right[i] = stack[-1]
            stack.append(i)


        pq = []
        for i in range(n):
            a = i-to_left[i]
            b = to_right[i] - i
            valid_subarray_length = a+b-1
            heapq.heappush(pq, (-nums[i], valid_subarray_length))

        ans = [-1]*n
        for i in range(n):
            while pq[0][1] < i+1:
                heapq.heappop(pq)
            ans[i] = -pq[0][0]
        return ans

        