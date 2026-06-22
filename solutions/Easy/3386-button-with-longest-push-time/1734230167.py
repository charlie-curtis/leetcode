class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:

        best_idx = events[0][0]
        best_val = events[0][1]
        n = len(events)
        for i in range(1,n):
            idx, j = events[i]
            k = events[i-1][1]
            if j - k > best_val:
                best_val = j-k
                best_idx = idx
            elif j-k == best_val and idx < best_idx:
                best_val = j-k
                best_idx = idx

        return best_idx
                
        