class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        d = {}

        for li in pieces:
            d[li[0]] = li



        n = len(arr)
        i = 0
        while i < n:
            need = arr[i]
            if need not in d:
                return False
            li = d[need]
            if i+len(li) > n:
                return False
            if li != arr[i:i+len(li)]:
                return False
            i+=len(li)
        return True


        
        