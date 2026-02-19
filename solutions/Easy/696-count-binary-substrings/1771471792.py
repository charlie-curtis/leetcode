class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        #since this problem only cares about consecutive characters, count the length of each consecutive group and compare it to its neighbor, taking the smaller of the two
        #11001100 -> this becomes [2,2,2,2], and the first 3 indices will sum to 6
        #11011 -> this becomes [2,1,2] and the first two indices sum to 2
        A = []
        for c, g in groupby(s):
            A.append(len(list(g)))
        
        ans = 0
        for i in range(len(A)-1):
            ans+=min(A[i], A[i+1])
        return ans
        