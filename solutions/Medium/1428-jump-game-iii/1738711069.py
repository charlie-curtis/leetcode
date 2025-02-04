class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:


        q = [start]

        if arr[start] == 0:
            return True
        seen = set()
        cnt = 0
        seen.add(start)
        n = len(arr)
        while q:
            idx = q.pop()
            if idx < 0 or idx >= n:
                continue
            
            if arr[idx] == 0:
                return True
            if idx - arr[idx] not in seen:
                q.append(idx-arr[idx])
                seen.add(idx-arr[idx])
            if idx + arr[idx] not in seen:
                q.append(idx+arr[idx])
                seen.add(idx+arr[idx])
        return False
        