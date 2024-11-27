class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:

        if k == 1:
            return True


        #I certainly missed some edge cases with this one. The important thing to note is that the first index and the last index is fixed. Our hand is forced because we need to make the first index equal to 0, and that causes us to subtract a certain amount. If that amount causes any of the preceeding k-1 numbers to go negative, then return False. The case that I missed is that the last index is also forced too. Since all of the numbers before it are already 0, we cannot touch the last element. We can only observe whether the last element is equal to cur (which represents how many deletes we've done in our window of size k)
        def good(A):
            n = len(A)
            d = defaultdict(int)
            cur = 0
            for i in range(n-1):
                cur +=d[i]
                if cur > A[i]:
                    return False
                A[i]-=cur
                cur+=A[i]
                d[i+k]-=A[i]
                A[i] = 0

            print(A)

            cur+=d[n-1]
            return nums[n-1] == cur
        return good(nums)

        