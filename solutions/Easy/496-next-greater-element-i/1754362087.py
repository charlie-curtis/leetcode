class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        m,n = len(nums1), len(nums2)
        nxt = {}
        stack = []
        for i in range(n-1, -1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                nxt[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        
        return [nxt[x] if x in nxt else -1 for x in nums1]

